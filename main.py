from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from pymongo import MongoClient
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import List
import uvicorn


client = MongoClient('mongodb://localhost:27017/')
db = client['job_search']
collection = db['job_postings']

SECRET_KEY = "abcxyz"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str

class Job(BaseModel):
    job_name: str
    company_name: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

@app.post("/signup")
async def signup(user: User):
    user_exists = db['users'].find_one({"email": user.email})
    print('came...')
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db['users'].insert_one({"email": user.email, "password": hashed_password})
    return {"msg": "User created successfully"}
 
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print('formdata->', form_data)
    user = db['users'].find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user['password']):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user['email']})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/jobs", response_model=List[Job])
async def get_jobs(title: str, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid authentication")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    jobs = collection.find({"job_name": {"$regex": title, "$options": "i"}})
    return [{"job_name": job["job_name"], "company_name": job["company_name"]} for job in jobs]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

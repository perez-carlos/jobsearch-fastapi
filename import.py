import pandas as pd
from pymongo import MongoClient

# Load the Excel file
file_path = 'dummy_data.xlsx'
df = pd.read_excel(file_path)

try:
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['job_search']
    collection = db['job_postings']

    # Clear existing data to avoid duplicates (optional)
    collection.delete_many({})

    # Convert DataFrame to dictionary and insert into MongoDB
    data = df.to_dict(orient='records')
    result = collection.insert_many(data)
    print(f"Data imported successfully! {len(result.inserted_ids)} records added.")
except Exception as e:
    print(f"An error occurred: {e}")

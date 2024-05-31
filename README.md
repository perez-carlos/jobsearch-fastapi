# FastAPI Job Search Backend

This backend service is built using FastAPI to support a job search application. It includes endpoints for user authentication and job searching functionalities. The backend is designed to interact with a MongoDB database, where job postings are stored.

## Features

- **User Authentication**: Support for user signup and login.
- **Job Search**: Allows users to search for jobs based on job titles.
- **Data Import**: A script to import job postings from an Excel file into MongoDB.

## Installation and Setup

Follow these instructions to get the backend up and running on your local machine.

### Prerequisites

- **Python**: Ensure Python is installed on your system. Visit [Python's website](https://www.python.org/downloads/) to download and install it if you haven't already.
- **MongoDB**: This project requires MongoDB to be installed and running on your local machine or a remote server. Visit [MongoDB's website](https://www.mongodb.com/try/download/community) to download and install it.
- **Pipenv**: This project uses Pipenv for managing dependencies and virtual environments. Install it via pip if it's not installed:
  ```bash
  pip install pipenv
  ```

### Setting Up Your Local Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/wevdev85/jobsearch-fastapi.git
   cd <colned dir>
   ```

2. **Install Dependencies**
   - Activate the virtual environment and install dependencies:
     ```bash
     pipenv install
     ```


### Running the Application

1. **Activate the Pipenv Shell**
   ```bash
   pipenv shell
   pipenv sync
   pipenv install
   ```(or you can use the requirements.txt to install packages dependancies to the project.

2. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Import Data**
   - Run the import script to load job postings from an Excel file into MongoDB:
     ```bash
     python import.py
     ```

## Usage

Once the server is running, you can access the API at [http://localhost:8000](http://localhost:8000). The following endpoints are available:

- `POST /signup`: Registers a new user.
- `POST /login`: Authenticates a user and returns an access token.
- `GET /jobs`: Fetches jobs based on the provided title query.

## Importing Data

- **File Format**: The data import script expects an Excel file named `Example job post data.xlsx` located in the project's root directory.
- **Script Execution**: Execute the script as shown in the running section to populate your MongoDB database.

## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **MongoDB**: A NoSQL database used for storing job postings.
- **Pandas**: A library for data manipulation and analysis, used in the data import script.
- **Uvicorn**: An ASGI server for running FastAPI.

---

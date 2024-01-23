# Infilect SDE Internship Assignment

## Problem Statement:
You are given a matrix of integers. Your task is to find the largest rectangle formed by similar
numbers in the matrix. A rectangle is defined by selecting a group of adjacent cells that contain
the same number. The rectangle should have the maximum area among all rectangles formed
by similar numbers.


Create a Fast API service that accepts the matrix on a POST API and returns the largest
rectangle’s area and the number itself.


## Prerequisites:
 
• Python 3.6+ <br>
• Virtual Environment

## Set up a Virtual Environment
    python -m venv venv
    On Windows use `venv\Scripts\activate`

## Install dependencies
    pip install -r requirements.txt

   
## Configure your MySQL connection in database.py
    URL_Database = 'mysql://{username}:{password}@localhost:{port}/{schema_name}'

## Running the Application
    uvicorn main:app --reload

   

Built With: <br>
  <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a> - The web framework used <br>
  <a href="https://www.sqlalchemy.org/" target="_blank">SQLAlchemy</a> - ORM and database toolkit <br>
  <a href="https://www.uvicorn.org/" target="_blank">Uvicorn</a> - ASGI server <br>


# Steps taken to complete the assignment:

## 1. Writing the Main Logic for Finding the Largest Rectangle in a Matrix:

Developed a Python function largest_rectangle(matrix) to find the largest rectangle formed by similar numbers in a 2D matrix.
The function iterates through the matrix, calculating the area of potential rectangles, and returns the largest area and the number that forms it.


## 2.Setting Up a FastAPI Application:
Created a FastAPI application to expose the largest_rectangle functionality as an API endpoint.
The FastAPI service includes a POST endpoint /largest-rectangle that accepts a matrix in JSON format and returns the result of the largest_rectangle function.


## 3. Database Integration:
Set up a connection to a MySQL database using SQLAlchemy ORM.
Created SQLAlchemy models to represent the data structure for logging requests and responses in the database.
Configured the database connection in database.py and defined the database model in models.py.


## 4. Creating Loggers:

Implemented a logging function log_to_database in logger.py to log request and response details, including processing time, to the MySQL database.
The logger captures request body, response body, and processing time.

## 5. Creating Middleware for Logging:

Developed a middleware function log_requests_middleware in middleware.py to intercept incoming requests and outgoing responses.
The middleware captures request details, passes the request to the next handler (call_next), captures response details, logs the data using log_to_database, and then returns the response.
The middleware is added to the FastAPI application to automatically log all requests and responses.

## 6.Running and Testing the Application:
Running the FastAPI server using Uvicorn and testing the API endpoints using Postman.

## API Endpoint (POST)
    http://127.0.0.1:8000/input-rectangle


## Sample request:
    {
    "matrix": [
        [1,1,1,1,1,1],
        [1,1,1,0,0,0],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]
    ]
    }  

## Sample Response:
    [1, 18]
     


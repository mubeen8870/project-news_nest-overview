  # News Nest – FastAPI News Manager with Live News Integration

# Project Overview
"NewsNest" is a backend application that helps manage news articles. It is built using FastAPI, a modern and fast web framework. The system allows users to add, update, view, delete, search, and count news articles stored locally in JSON format. Additionally, it can fetch live news from an external source like NewsAPI.org."


## Part 1: 
## ✅ What is FastAPI?
Fast API is a high-performance Python web framework used for building RESTful APIs quickly and efficiently. It is built on Starlette (for web handling) and Pydantic (for data validation).

## 🔑 Features:
Fast: Comparable to Node.js and Go in performance.
Easy to Use: Automatic docs and strong typing.
Data Validation: Uses Pydantic to ensure correct input.
Async Ready: Supports async/await for concurrency.
Interactive Docs: Swagger UI and ReDoc included by default.

## ✅ What is Pydantic?
Pydantic is a Python library used for data validation using Python type annotations. It ensures that the input data matches the expected format.
Example:
```python
Copy
Edit
from Pydantic import BaseModel
Class News (BaseModel):
    id: int
    title: str
    content: str
    author: str
```

---


## ✅ What is Uvicorn?
Uvicorn is an ASGI server for running FastAPI applications. It is lightweight and extremely fast.

### Command to run:

bash
Copy
Edit
uvicorn main:app --reload

## ✅ What is a JSON Database?
Instead of using SQL or NoSQL, we store data in a database.json file — a lightweight and easy format for simple data storage.

## Part 2: Step-by-Step Project Overview
 * 1. What Is the Project About?
This is a backend news management system using FastAPI.

 ### Features:
CRUD operations for news
Store data in a local JSON file
Fetch live news from an external API (like NewsAPI.org)

* 2. What Are We Doing in This Project?
### Step-by-step workflow:

* Create a FastAPI backend app

* Design models using Pydantic

* Organize the app into:

* main.py – App entry

* news_routes.py – All endpoints

* schemas.py – Data models

* external_service.py – External API logic

* Store data in database.json

* Run the project using Uvicorn

## Test via Swagger UI or Postman

 ### 3. How to Start the Project

 * Step 1: Open Terminal / Anaconda Prompt
bash
Copy
Edit
cd path_to_your_project_folder

* Step 2: Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt

* Step 3: Run FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload

* Step 4: Test Using Swagger UI
Open in browser:

arduino
Copy
Edit
http://127.0.0.1:8000/docs


## 4. Where Is Data Stored?
All news data is saved in database.json:
json
[
  {
    "id": 1,
    "title": "Global Tech Update",
    "content": "Technology market is booming.",
    "author": "Salman"
  }
]


## 5. Which Model Are We Using?
We use a Pydantic model in schemas.py:
```Python
Class News(BaseModel):
    id: int
    title: str
    content: str
    author: str

```

---

## 6. What Commands Are Used?
### Command:
Install packages  pip install -r requirements.txt
Run FastAPI server  uvicorn main:app --reload
Open Swagger docs http://127.0.0.1:8000/docs



## 7. Project Folder Structure!
### PGSQL
newsnest/
├── main.py                → Starts the FastAPI app
├── news_routes.py         → Contains all 8 API endpoints
├── schemas.py             → Data model using Pydantic
├── external_service.py    → Fetches live news from external API
├── database.json          → Stores local news data
├── requirements.txt       → List of required libraries
└── __init__.py            → (Optional)


## 8. What Are the 8 Endpoints?
Method   Endpoint   Description
* POST  /news/  Add new news
* GET /news/  View all news
* GET /news/{id}  View specific news by ID
* PUT /news/{id}  Update news
* DELETE  /news/{id}  Delete news
* GET /news/search/ Search news by title
* GET /news/count/  Count all news
* GET /news/live/ Fetch live news from external API



## 9. Explanation
**“We built a FastAPI-based backend called NewsNest that manages news articles stored locally in JSON. It supports full CRUD operations, allows keyword-based search, and  integrates with an external API to fetch real-time news. The app is organized into modular files and can be tested via Swagger or Postman.”**




## Questions?
* 1.  What is the main goal of the NewsNest project?
* 2.  Why did you choose FastAPI for building this application?
* 3. What are the 8 API endpoints included in this project?
* 4. How is the data stored and managed locally?
* 5. What is the role of Pydantic in this project?
* 6. How does the project fetch live news from external sources?
* 7. What is the function of each major Python file (e.g., main.py, news_routes.py, etc.)?
* 8. How do you run and test the FastAPI application?


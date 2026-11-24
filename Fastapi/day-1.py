# mkdir folder_name_of_project  ---> create a new folder for the project
# cd folder_name_of_project   ----> change directory to the new project folder
# python -m venv venv       ----> create a virtual environment named 'venv'
# venv\Scripts\activate     ----> activate the virtual environment (Windows)
# pip install fastapi uvicorn    ---> install FastAPI and Uvicorn (ASGI server)
# pip show fastapi   ----> check if fastapi is installed then what version is installed

# uvicorn file_name:app --reload   ----> run the FastAPI application with auto-reload enabled

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}
  
@app.get("/about")
def about_page():
    return {
      "message": "This is my about page of FastAPI application!",
      "project": "FastAPI"
      }

  
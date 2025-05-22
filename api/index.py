from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Marks API is working!"}

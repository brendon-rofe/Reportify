from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Reportify API!"}

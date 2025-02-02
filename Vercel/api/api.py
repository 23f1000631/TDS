from fastapi import FastAPI, Query
import json
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from JSON file
with open("marks.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    """
    API Endpoint: Fetch marks for given student names.
    
    Example request:
    https://your-app.vercel.app/api?name=Alice&name=Bob

    Example response:
    { "marks": [85, 92] }
    """
    result = {"marks": [marks_data.get(n, None) for n in name]}
    return result

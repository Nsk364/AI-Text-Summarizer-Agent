from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class RequestData(BaseModel):
    text: str

OLLAMA_API_URL = "http://localhost:11434/api/generate"

@app.post("/summarize/")
async def summarize(request: RequestData):
    try:
        response = requests.post(OLLAMA_API_URL, json={"model": "deepseek-r1:7b", "prompt": request.text})
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run with: uvicorn app:app --reload

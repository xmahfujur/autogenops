from fastapi import FastAPI
from pydantic import BaseModel
from google import generativeai as genai
from backend.config import GEMINI_API_KEY


app = FastAPI()

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = model.generate_content(
        f'You are a helpful AI assistant. \nUser: {request.message}'
    )

    return {
        "response": response.text
    }
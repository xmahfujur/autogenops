from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import generativeai as genai
from backend.config import GEMINI_API_KEY

app = FastAPI()

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model once (global)
model = genai.GenerativeModel("gemini-1.5-flash")


# Request schema
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)


# Response schema (optional but clean)
class ChatResponse(BaseModel):
    response: str


# System prompt (separate for maintainability)
SYSTEM_PROMPT = "You are a helpful, concise AI assistant."


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        prompt = f"{SYSTEM_PROMPT}\nUser: {request.message}"

        result = model.generate_content(prompt)

        # Handle empty or blocked response
        if not result or not result.text:
            return ChatResponse(response="No response generated. Try again.")

        return ChatResponse(response=result.text)

    except Exception as e:
        # Log this in real systems
        raise HTTPException(status_code=500, detail=str(e))
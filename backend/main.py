from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from backend.config import GEMINI_API_KEY

app = FastAPI()

client = genai.Client(api_key=GEMINI_API_KEY)

class CharRequest(BaseModel):
    message : str
    
class ResponseChat(BaseModel):
    response : str

SYSTEM_PROMPT = 'You are a helpful multi-agent AI assistant.'


@app.post('/chat', response_model=ResponseChat)
async def chat(request : CharRequest):
    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = [
            {'role': 'user', 'parts': [SYSTEM_PROMPT]},
            {'role': 'user', 'parts': [request.message]}
        ]
    )
    
    return ResponseChat(response=response.text)
    
from fastapi import UploadFile, File, HTTPException
import shutil
import os

UPLOAD_DIR = 'backend/uploads'

@app.post('/upload-doc')
async def upload_doc(file : UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    
        with open(file_path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {
            'message' : 'File uploaded successfully', 
            'filename' : file.filename
        }
    except:
        raise HTTPException(status_code=500, detail='bad request')
    
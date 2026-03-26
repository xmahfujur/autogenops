from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai
from .config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)
app = FastAPI()

class ChatRequest(BaseModel):
    message : str 

class ChatResponse(BaseModel):
    reply : str

MODEL_NAME = 'gemini-2.5-flash'

@app.post("/chat" , response_model=ChatResponse)
async def chat(req : ChatRequest):
   
   try:
       response = genai.models.generate_content(
           model=MODEL_NAME,
           contents=req.message
       )

       return ChatResponse(reply=response.text)
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))



from fastapi import UploadFile, File
import shutil
import uuid
import os

UPLOAD_DIR = 'backend/uploads'

@app.post('/upload-doc')
async def upload_doc(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    unique_name = f'{uuid.uuid4()}_{file.filename}'
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {'message':'File uploaded successfully', 'filename': file.filename}

print(chat('hello world'))
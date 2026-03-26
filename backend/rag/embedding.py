from google import genai
from backend.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def get_embedding(text: str):
    try:
        result = client.models.embed_content(
            model="models/embedding-004",
            contents=text
        )
        return result.embedding.values

    except Exception as e:
        print(f"Embedding error: {e}")
        return None
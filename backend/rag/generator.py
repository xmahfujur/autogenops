from google import genai
from backend.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = 'gemini-2.5-flash'
def generate_answer(query, contexts):
    context_text = "\n\n".join(contexts)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context_text}

    Question:
    {query}
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text



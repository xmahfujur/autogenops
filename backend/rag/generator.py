from google import genai
from backend.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = 'gemini-2.5-flash'
def generate_answer(query, contexts):
    context_text = "\n\n".join(contexts)

    prompt = f"""
You are a strict AI assistant.

Rules:
1. Answer ONLY from the provided context
2. If answer is not in context → say "I don't know"
3. Do NOT guess
4. Be concise and accurate
    Context:
    {context_text}

    Question:
    {query}
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return {
        'answer': response.text,
        'source' : contexts
    }



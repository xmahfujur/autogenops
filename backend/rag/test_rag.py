from .loader import document_loader
from .chunker import chunk_documents
from .vector_store import SimpleVectorStore
from .generator import generate_answer
from google import genai
from backend.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

model = client.models.list()

# for i in model:
#     print(i.name)
docs = document_loader('backend/uploads')
nodes = chunk_documents(docs)

store = SimpleVectorStore()
store.add(nodes)

query = 'What is the document about?'

context = store.search(query)

answer = generate_answer( query, context)

print("answer:\n", answer)
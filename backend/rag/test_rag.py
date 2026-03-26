from .loader import document_loader
from .chunker import chunk_documents
from .vector_store import SimpleVectorStore
from .generator import generate_answer

docs = document_loader('backend/uploads')
nodes = chunk_documents(docs)

store = SimpleVectorStore()
store.add(nodes)

query = 'What is the document about?'

context = store.search(query)

answer = generate_answer( query, context)

print("answer:\n", answer)
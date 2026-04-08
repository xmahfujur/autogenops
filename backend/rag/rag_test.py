from .loader import document_loader
from .chunker import chunk_document
from .vector_store import create_index, create_query_engine

docs = document_loader('backend/uploads')
nodes = chunk_document(docs)
index = create_index(nodes)
query_engine = create_query_engine(index)

response = query_engine.query("what is the document about")

print(response) 
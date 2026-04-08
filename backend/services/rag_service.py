from backend.rag.loader import document_loader
from backend.rag.chunker import chunk_document
from backend.rag.vector_store import create_index, create_query_engine

class RAGService:
    def __init__(self):
        self.index = None
        self.query_engine = None
        
    def load_data(self):
        docs = document_loader('backend/uploads')
        nodes = chunk_document(docs)
        
        self.index = create_index(nodes)
        self.query_engine = create_query_engine(self.index)
        
    def query(self, query: str):
        if not self.query_engine:
            return {'error' : 'No documents loaded'}
        
        response = self.query_engine.query(self.query)
        
        return {
            'answer' : response.response,
            'sources' : [node.text for node in response.source_nodes]
            
        }
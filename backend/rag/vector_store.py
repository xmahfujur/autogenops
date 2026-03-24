from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss

def create_vector_store(nodes):

    dimension = 1536
    faiss_index = faiss.IndexFlatL2(dimension)

    vector_store = FaissVectorStore(faiss_index=faiss_index)

    index = VectorStoreIndex(
        nodes,
        vector_store = vector_store

    )
    return index

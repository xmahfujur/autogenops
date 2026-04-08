from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex , Settings
from backend.config import GEMINI_API_KEY
from llama_index.llms.gemini import Gemini

embed_model = HuggingFaceEmbedding(
     model_name='BAAI/bge-small-en'
)


llm = Gemini(
    model = 'gemini-3-flash-preview',
    api_key=GEMINI_API_KEY
)

Settings.embed_model = embed_model
Settings.llm = llm

def create_index(nodes):
    index = VectorStoreIndex(
        nodes,
        embed_model=embed_model
    )
    return index


def create_query_engine(index):
    return index.as_query_engine(
        similarity_top_k = 5
    )

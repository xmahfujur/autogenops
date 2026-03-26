from .loader import document_loader
from llama_index.core.node_parser import SentenceSplitter

def chunk_documents(documents):
    splitter = SentenceSplitter(
        chunk_size=600,
        chunk_overlap=100
    )
    nodes = splitter.get_nodes_from_documents(documents)
    return nodes

docs = document_loader('backend/uploads')
nodes = chunk_documents(docs)

# print(len(nodes))
# print(nodes[1].text)
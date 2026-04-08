from llama_index.core.node_parser import SentenceSplitter

def chunk_document(document):
    parser = SentenceSplitter(
        chunk_size=512,
        chunk_overlap=50
    )
    
    nodes = parser.get_nodes_from_documents(document)
    return nodes
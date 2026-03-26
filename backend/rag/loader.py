from llama_index.core import SimpleDirectoryReader

def document_loader(path : str):
    docs = SimpleDirectoryReader(path).load_data()
    return docs

data = document_loader('backend/uploads')
# print(data[0].text[:1000])
    
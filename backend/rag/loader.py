from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PyMuPDFReader

file_extractor = {
    '.pdf' : PyMuPDFReader()
}

def document_loader(path: str):
    documents = SimpleDirectoryReader(
        input_dir=path,
        file_extractor=file_extractor
    ).load_data()
    
    return documents
docs = document_loader('backend/uploads')
# if docs:
#     print(docs[0].text[:500])
# else:
#     print('No file')

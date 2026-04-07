from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader
from llama_index.readers.file import PyMuPDFReader
import fitz
file_extractor = {
    '.pdf' : PyMuPDFReader(),
}

docs = SimpleDirectoryReader(
    input_dir='backend/uploads',
    file_extractor=file_extractor
).load_data()

print(docs[0].text[:200])

import os
import fitz

def load_documents(directory):
    documents = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        doc = fitz.open(file_path)
        for page in doc:
            text = page.get_text()
            documents.append(text)

        if not filename.endswith('.pdf')

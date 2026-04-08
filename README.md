# 🚀 AutogenOps

**A Production-Oriented RAG (Retrieval-Augmented Generation) System with Gemini + LlamaIndex**

---

## 📌 Overview

**AutogenOps** is a modular GenAI system designed to **ingest documents, build semantic understanding, and answer user queries using LLMs**.

It combines:

* 📄 Document ingestion (PDF support)
* ✂️ Intelligent chunking
* 🧠 Embedding-based semantic search
* ⚡ Vector indexing
* 🤖 LLM-powered responses (Gemini)

---

## 🧠 Architecture

```text
Documents (PDFs)
        ↓
SimpleDirectoryReader
        ↓
SentenceSplitter (Chunking)
        ↓
Embeddings (HuggingFace - BGE)
        ↓
Vector Store Index
        ↓
Query Engine (Gemini LLM)
        ↓
Final Answer
```

---

## ⚙️ Tech Stack

| Layer           | Technology                                     |
| --------------- | ---------------------------------------------- |
| Framework       | LlamaIndex                                     |
| LLM             | Google Gemini                                  |
| Embedding Model | BAAI/bge-small-en                              |
| Vector Store    | SimpleVectorStore (default) / FAISS (optional) |
| Backend         | Python                                         |
| API (optional)  | FastAPI                                        |

---

## 📁 Project Structure

```text
AutogenOps/
│
├── backend/
│   ├── uploads/              # Uploaded documents
│   ├── config.py             # API keys (Gemini)
│
├── ingestion/
│   ├── loader.py             # Document loading
│   ├── chunking.py           # Sentence splitting
│
├── indexing/
│   ├── embedder.py           # Embedding model
│   ├── index_builder.py      # Vector index creation
│
├── query/
│   ├── query_engine.py       # Query logic with Gemini
│
├── main.py                   # Entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Features

* ✅ PDF document ingestion
* ✅ Sentence-based chunking with overlap
* ✅ Local embedding (no OpenAI cost)
* ✅ Gemini-powered answering
* ✅ Modular architecture (production-ready design)
* 🔄 Optional FAISS integration for scalable search

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AutogenOps.git
cd AutogenOps
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `config.py` inside `backend/`:

```python
GEMINI_API_KEY = "your_api_key_here"
```

---

## ▶️ Usage

### 1. Add documents

Place your PDFs inside:

```text
backend/uploads/
```

---

### 2. Run pipeline

```python
docs = document_loader('backend/uploads')
nodes = chunk_documents(docs)
index = create_index(nodes)

query_engine = create_query_engine(index)

response = query_engine.query("What is this document about?")
print(response)
```

---

## 🧪 Example Query

```text
Input:  "Explain the main concept of the document"
Output: "The document discusses..."
```

---

## ⚡ Optional: FAISS Integration

For scalable vector search:

```bash
pip install faiss-cpu
```

Replace default vector store with FAISS for:

* Faster retrieval
* Large dataset support
* Production deployment



## 📈 Future Improvements

* 🔥 Add chat memory (multi-turn conversation)
* 🔥 Multi-document retrieval system
* 🔥 Reranking (BGE reranker)
* 🔥 Web UI (Streamlit / React)
* 🔥 Deployment (Docker + Cloud)



## 🎯 Learning Goals

This project demonstrates:

* RAG system design
* Embedding-based retrieval
* LLM integration (Gemini)
* Modular GenAI architecture



## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.



## 📜 License

MIT License



## 🌟 Acknowledgements

* LlamaIndex
* HuggingFace
* Google Gemini



## 💡 Author

**Scientist**
Aspiring GenAI Engineer & Researcher 🚀



> ⚡ *AutogenOps is a step toward building scalable, intelligent AI systems.*

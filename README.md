# RAG Chatbot with Qwen Model

## 📖 Overview
This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with FAISS indexing and the Qwen language model.  
It combines **semantic search** with **generative AI** to deliver accurate, context‑aware answers from domain‑specific documents.

## 🚀 Features
- Multilingual support using LaBSE embeddings
- FAISS vector database for fast similarity search
- PDF/Text ingestion with automatic chapter splitting
- Modular design (`Modules/` folder keeps logic clean)
- Interactive chatbot interface (`chatbot.py` and `main.py`)

## 🛠️ Tech Stack
- Python 3.10+
- [LangChain](ca://s?q=Tell_me_about_LangChain) for orchestration
- [FAISS](ca://s?q=Explain_FAISS) for vector search
- [Sentence Transformers](ca://s?q=Sentence_Transformers_overview) for embeddings
- [Qwen](ca://s?q=Qwen_model_details) as the generative model

## 📂 Project Structure
RAG_Chatbot/
│── Data/                # Source PDFs and text files
│── Modules/             # Core logic (chat_engine, index_builder, etc.)
│── faiss_index/         # Saved FAISS index
│── Utils/               # Helper scripts
│── main.py              # Entry point
│── chatbot.py           # Chatbot runner
│── requirements.txt     # Dependencies
│── README.md            # Project documentation


## ⚡ Getting Started
1. Clone the repo:
   ```bash
   git clone https://github.com/Navneet-code605/RAG_Chatbot_Qwen.git
   cd RAG_Chatbot_Qwen

2. Create a virtual environment:
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Run the Chatbot
python main.py


📌 Future Improvements
1. Web UI integration
2. Real‑time data sources
3. Deployment on cloud platforms
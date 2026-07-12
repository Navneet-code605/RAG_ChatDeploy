import sys
print(sys.executable)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from Modules.pdf_loader import load_text_files, split_documents

def build_index(data_folder="Data", index_path="faiss_index"):
    documents = load_text_files(data_folder)
    chunks = split_documents(documents)

    # ✅ Use LaBSE (stable multilingual embeddings)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/LaBSE")

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)
    print(f"✅ Index built with LaBSE embeddings at {index_path}")
 
 # Return FAISS index and texts for query_engine
    return vectorstore.index, [doc.page_content for doc in chunks]

if __name__ == "__main__":
    build_index()


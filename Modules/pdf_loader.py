import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_text_files(data_folder="Data"):
    documents = []
    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append(Document(page_content=text, metadata={"source": filename}))
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

if __name__ == "__main__":
    docs = load_text_files("Data")
    chunks = split_documents(docs)
    print(f"✅ Loaded {len(docs)} documents and split into {len(chunks)} chunks")

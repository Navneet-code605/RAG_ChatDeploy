import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from Modules.pdf_loader import load_text_files, split_documents


def create_index(data_folder="Data", index_path="faiss_index"):

    documents = load_text_files(data_folder)
    chunks = split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/LaBSE"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(index_path)

    print(f"✅ Index created and saved to {index_path}")


def load_index(index_path="faiss_index"):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/LaBSE"
    )

    vectorstore = FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("✅ Existing FAISS index loaded")

    return vectorstore


if __name__ == "__main__":
    create_index()
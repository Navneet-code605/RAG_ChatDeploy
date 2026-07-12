import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from Modules.query_engine import query_engine

class ChatEngine:
    def __init__(self, index, texts, preferred_lang="English"):
        self.index = index
        self.texts = texts
        self.history = []
        self.preferred_lang = preferred_lang

    def chat(self, query):
        answer = query_engine(query, self.index, self.texts, preferred_lang=self.preferred_lang)
        self.history.append({"query": query, "answer": answer})
        return answer

# ✅ Test block
if __name__ == "__main__":
    from Modules.pdf_loader import load_text_files, split_documents
    from Modules.index_builder import build_index

    # Build FAISS index directly from Data folder
    index, texts = build_index("Data")

    chat = ChatEngine(index, texts)

    print("Chatbot ready! Type your questions below.")
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = chat.chat(query)
        print("Answer:\n", answer)

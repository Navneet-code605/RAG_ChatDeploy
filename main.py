import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from Modules.index_builder import build_index
from Modules.chat_engine import ChatEngine

def main():
    # Build FAISS index directly from Data folder (using index_builder)
    index, texts = build_index("Data")

    # Initialize chat engine
    chat = ChatEngine(index, texts)

    print("🩺 Medical Chatbot here to resolve your query!")
    preferred_lang = input("Please tell me your preferred language :: ")
    chat.preferred_lang = preferred_lang if preferred_lang else "English"
    print(f"Great! I’ll answer in {chat.preferred_lang}. Now ask your question below.")

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Stay healthy.")
            break
        answer = chat.chat(query)
        print("Answer:\n", answer)

if __name__ == "__main__":
    main()

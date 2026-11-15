import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from Modules.index_builder import build_index
from Modules.chat_engine import ChatEngine

# --- STT and TTS imports ---
#import speech_recognition as sr
#import pyttsx3

# --- Speech-to-Text function ---
def speech_to_text():
            return None

# --- Text-to-Speech function ---
def text_to_speech(text):
    pass

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
        mode = "type"
        if mode in ["exit", "quit"]:
            print("👋 Goodbye! Stay healthy.")
            break

        query = input("\nAsk a question: ")

        answer = chat.chat(query)
        print("Answer:\n", answer)

        # Speak out the answer
        text_to_speech(answer)

if __name__ == "__main__":
    main()


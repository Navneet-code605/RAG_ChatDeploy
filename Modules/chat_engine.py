import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from Modules.query_engine import query_engine
from langdetect import detect
#from deep_translator import GoogleTranslator

class ChatEngine:
    def __init__(self, index, texts, preferred_lang="English"):
        self.index = index
        self.texts = texts
        self.history = []
        self.preferred_lang = preferred_lang

    def detect_language(self, query):
        try:
            lang_code = detect(query)   # e.g. 'hi', 'en', 'fr', 'es'
            return lang_code
        except:
            return "en"  # fallback

    def translate_context(self, passages, target_lang):
            return passages

    def chat(self, query):
        # Step 1: detect user query language
        user_lang = self.detect_language(query)

        # Step 2: retrieve context (English docs)
        retrieved_passages = self.texts  # or however your query_engine pulls docs

        # Step 3: translate context if needed
        context = self.translate_context(retrieved_passages, user_lang)

        # Step 4: call query_engine with detected language
        answer = query_engine(query, self.index, context, preferred_lang=user_lang)

        # Step 5: save history
        self.history.append({"query": query, "answer": answer, "lang": user_lang})
        return answer

# ✅ Test block
if __name__ == "__main__":
    from Modules.index_builder import build_index
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

from Modules.query_engine import query_engine

class ChatBot:
    def __init__(self, index, texts, preferred_lang="English"):
        self.index = index
        self.texts = texts
        self.preferred_lang = preferred_lang
        self.history = []

    def ask(self, query):
        """Ask a question and get an answer in the preferred language."""
        answer = query_engine(query, self.index, self.texts, preferred_lang=self.preferred_lang)
        self.history.append({"query": query, "answer": answer})
        return answer

    def get_history(self):
        """Return the full Q&A history."""
        return self.history

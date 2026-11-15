import streamlit as st

from Modules.index_builder import build_index
from Modules.chat_engine import ChatEngine

st.set_page_config(
    page_title="Multilingual RAG Chatbot",
    page_icon="🤖"
)

@st.cache_resource
def load_chatbot():
    index, texts = build_index("Data")
    return ChatEngine(index, texts)

chat = load_chatbot()

st.title("🤖 Multilingual RAG Chatbot")

st.write("Ask questions in English, Hindi, or Punjabi.")

query = st.text_input("Enter your question:")

if query:
    answer = chat.chat(query)

    st.subheader("Answer")
    st.write(answer)
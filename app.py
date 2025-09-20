# app.py
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# ========================
# Setup API Key
# ========================
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("🚨 GOOGLE_API_KEY not found! Please set it in environment variables.")
    st.stop()

# ========================
# Configure Chat Model
# ========================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    convert_system_message_to_human=True,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)



prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Library Assistant. Answer clearly and politely."),
    ("user", "{question}")
])
chain = LLMChain(llm=llm, prompt=prompt)

# ========================
# Streamlit UI
# ========================
st.set_page_config(page_title="📚 Library Palm Chatbot", page_icon="🤖", layout="centered")

st.title("📚 Library Palm Chatbot")
st.markdown("🤖 Ask me anything about the library, books, authors, or borrowing rules!")

# Chat history (session state)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Type your question here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = chain.run(question=user_input)
            st.markdown(response)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": response})

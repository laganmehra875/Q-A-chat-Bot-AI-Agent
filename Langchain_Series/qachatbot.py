import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables from .env file
load_dotenv()

# Get Groq API Key from environment variables
api_key = os.getenv("GROQ_API_KEY", "")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Simple LangChain Chatbot with Groq",
    page_icon="🚀",
    layout="centered"
)

# -----------------------------
# App Header
# -----------------------------
st.title("🚀 Simple LangChain Chatbot with Groq")
st.markdown("Learn LangChain basics with Groq's ultra-fast inference!")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model_name = st.selectbox(
        "Select Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "gemma2-9b-it"
        ]
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Load LLM
# -----------------------------
@st.cache_resource
def load_llm(api_key, model_name):
    return ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=0.3,
        streaming=True,
        max_tokens=1024
    )

# -----------------------------
# API Key Check
# -----------------------------
if not api_key:
    st.error("❌ Groq API Key not found! Please set the `GROQ_API_KEY` in your `.env` file to start chatting.")
    st.stop()

try:
    llm = load_llm(api_key, model_name)
except Exception as e:
    st.error(f"Failed to initialize model: {e}")
    st.stop()

# -----------------------------
# Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation history
    history = []

    for msg in st.session_state.messages[:-1]:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        else:
            history.append(AIMessage(content=msg["content"]))

    history.append(HumanMessage(content=user_input))

    # Assistant Response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()
        full_response = ""

        try:
            for chunk in llm.stream(history):

                if hasattr(chunk, "content") and chunk.content:
                    full_response += chunk.content
                    response_placeholder.markdown(full_response + "▌")

            if not full_response.strip():
                full_response = (
                    "I'm sorry, I couldn't generate a response."
                )

            response_placeholder.markdown(full_response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        except Exception as e:
            error_message = f"❌ Error: {str(e)}"
            st.error(error_message)

# -----------------------------
# Examples
# -----------------------------
st.markdown("---")
st.subheader("💡 Try these examples")

col1, col2 = st.columns(2)

with col1:
    st.markdown("- What is LangChain?")
    st.markdown("- Explain RAG in simple words?")

with col2:
    st.markdown("- Give me a Data Science roadmap?")
    st.markdown("- Write a Python Fibonacci program?")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "Built with ❤️ using Streamlit, LangChain, and Groq"
)

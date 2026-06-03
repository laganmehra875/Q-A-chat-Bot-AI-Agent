# 🚀 Simple LangChain Q&A Chatbot with Groq

A beginner-friendly Streamlit chatbot application utilizing **LangChain** and **Groq** for ultra-fast response generation.

---

## ✨ Features

- ⚡ **Ultra-Fast Inference**: Powered by Groq's high-speed LLM engine.
- 🔄 **Session History**: Keeps track of active conversation messages.
- ⚙️ **Configurable Settings**: 
  - Dynamic model selection (e.g., Llama 3.3, Llama 3.1, Gemma 2).
  - Secure API Key input via Streamlit sidebar.
- 🛠️ **Environment Aware**: Automatically loads your `GROQ_API_KEY` from a local `.env` file for a seamless development experience.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/laganmehra875/Langchain_Series.git
cd Langchain_Series
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY="your_groq_api_key_here"
```

### 3. Install Dependencies
Make sure you have [uv](https://github.com/astral-sh/uv) or `pip` installed:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

To launch the Streamlit application:
```bash
streamlit run qachatbot.py
```

---

## 💡 Example Prompts to Try
- "What is LangChain?"
- "Explain RAG in simple words."
- "Write a Python Fibonacci program."

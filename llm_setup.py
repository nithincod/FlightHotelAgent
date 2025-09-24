from langchain.chat_models import ChatGroq

def get_llm():
    """
    Configure and return a free LLM (Groq in this case).
    Replace with HuggingFaceHub if preferred.
    """
    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0,
        groq_api_key="YOUR_GROQ_API_KEY"  # <-- replace with your key
    )
    return llm

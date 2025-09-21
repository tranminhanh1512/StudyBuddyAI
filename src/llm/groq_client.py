from langchain_groq import ChatGroq
from src.config.settings import settings

def get_groq_llm():
    return ChatGroq(
        api_key = settings.GROG_API_KEY,
        model = settings.MODEL_NAME,
        temperature = settings.TEMPERATURE,
    )
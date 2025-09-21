import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROG_API_KEY = os.getenv("GROG_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"
    TEMPERATURE = 0.9
    MAX_RETRIES = 3

settings = Settings()  
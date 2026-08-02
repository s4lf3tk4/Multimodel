from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
load_dotenv("environment.env")

BASE_URL = "https://api.chatanywhere.tech/v1"
API_KEY = os.getenv("CHATANYWHERE_API_KEY")

llm_gtp_40 = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=API_KEY,
    openai_api_base=BASE_URL,
    temperature=0.1
)

llm_mistral = ChatOllama(
    model="mistral",
    num_predict=2000
)

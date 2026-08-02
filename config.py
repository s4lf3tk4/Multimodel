from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
load_dotenv("environment.env")

BASE_URL = "https://api.chatanywhere.tech/v1"
API_KEY = os.getenv("CHATANYWHERE_API_KEY")

#code
llm_gpt_40 = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=API_KEY,
    openai_api_base=BASE_URL,
    temperature=0.1
)
#systematization
llm_gpt_54 = ChatOpenAI(
    model="gpt-5.4-mini",
    openai_api_key=API_KEY,
    openai_api_base=BASE_URL,
    temperature=0.1
)
#local
llm_gpt_41 = ChatOpenAI(
    model = "gpt-4.1-mini",
    openai_api_key=API_KEY,
    openai_api_base=BASE_URL,
    temperature=0.1
)

#dialog+analysis
llm_mistral = ChatOllama(
    model="mistral",
    num_predict=2000
)

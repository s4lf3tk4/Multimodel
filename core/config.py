from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from core.settings import settings

BASE_URL = settings.base_url
API_KEY = settings.chatanywhere_api_key

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
    base_url="http://localhost:11434",
    num_predict=2000
)

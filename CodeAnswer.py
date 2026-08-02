from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from bundle import SystemState
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage, AIMessage

load_dotenv("environment.env")

BASE_URL = "https://api.chatanywhere.tech/v1"
API_KEY = os.getenv("CHATANYWHERE_API_KEY")


llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=API_KEY,
    openai_api_base=BASE_URL,
    temperature=0.1
)

def codeAnswer(state: SystemState)->dict:
    user_input = state["current_message"]
    messages = [SystemMessage(content="Ты - программист с огромным стажем, дай краткий и информативный ответ")]+ state["messages"] + [HumanMessage(content = user_input)]
    response = llm.invoke(messages)
    result = response.content
    print(f"ИИ: {result}")
    new_messages = state["messages"]+ [AIMessage(content = result)]
    return {
        "messages": new_messages,
        "code": ""
    }

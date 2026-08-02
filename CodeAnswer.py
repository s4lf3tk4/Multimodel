from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from bundle import SystemState
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage, AIMessage
from config import llm_gtp_40
load_dotenv("environment.env")


def codeAnswer(state: SystemState)->dict:
    user_input = state["current_message"]
    messages = [SystemMessage(content="Ты - программист с огромным стажем, дай краткий и информативный ответ")]+ state["messages"] + [HumanMessage(content = user_input)]
    response = llm_gtp_40.invoke(messages)
    result = response.content
    print(f"ИИ: {result}")
    new_messages = state["messages"]+ [AIMessage(content = result)]
    return {
        "messages": new_messages,
        "code": ""
    }

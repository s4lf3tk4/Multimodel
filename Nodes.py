from bundle import SystemState, classification_prompt, classification_parser
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from CodeAnswer import codeAnswer
from config import llm_mistral

def userInput(state: SystemState)->dict:
    user_input = input("Вы: ").strip()
    if user_input.lower() in ["выход", "quit", "exit", "пока", "bye"]:
        return {"should_continue": False}
    if not user_input:
        print("Спросите что-нибудь")
        return {}
    new_messages = state["messages"]+ [HumanMessage(content = user_input)]
    return {
        "messages": new_messages,
        "current_message": user_input,
        "should_continue": True
    }

def classifyMessage(state: SystemState)-> dict:
    user_input = state["current_message"]
    classification_chain = classification_prompt | llm_mistral | classification_parser
    classification_result = classification_chain.invoke({"user_input": user_input})

    message_type = classification_result["message_type"]
    confidence = classification_result["confidence"]

    print(f"Тип сообщения: {message_type}, уверенность: {confidence}")
    return{
        "message_type": message_type,
    }

def systematization(state: SystemState)->dict:
    if state["code"]:
        print(1)
    if state["dialog"]:
        print(2)
    if state["local"]:
        print(3)

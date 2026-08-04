from core import SystemState, classification_prompt, classification_parser
from core import llm_mistral
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage

def userInput(state: SystemState)->dict:
    user_input = input("Вы: ").strip()
    if not user_input:
        print("Спросите что-нибудь")
        return {}
    new_messages = state["messages"]+ [HumanMessage(content = user_input)]
    return {
        "messages": new_messages,
        "current_message": user_input,
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

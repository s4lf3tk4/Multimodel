from bundle import SystemState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from config import llm_mistral

def dialog(state: SystemState)->dict:
    user_input = state["current_message"]
    messages = state["messages"]
    response = llm_mistral.invoke(messages)
    result = response.content
    print(f"ИИ(mistral): {result}")
    new_messages = state["messages"]+ [AIMessage(content = result)]
    return {
        "messages": new_messages,
        "dialog": result
    }

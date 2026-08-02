from bundle import SystemState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from config import llm_gpt_41

def localDialog(state: SystemState)->dict:
    user_input = state["current_message"]
    messages = [SystemMessage(content="Дай краткий и инофрмативный ответ по Российсикм реалиям")]+ state["messages"]
    response = llm_gpt_41.invoke(messages)
    result = response.content
    print(f"ИИ(gpt_41): {result}")
    new_messages = state["messages"]+ [AIMessage(content = result)]
    return {
        "messages": new_messages,
        "local": result
    }

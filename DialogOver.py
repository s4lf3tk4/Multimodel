from bundle import SystemState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from config import llm_mistral

def dialogOver(state: SystemState)->None:
    user_input = state["current_message"]
    messages = [SystemMessage(content="Лаконично попращяйся, пожелай успехов в задачах пользователя")]+ state["messages"]
    response = llm_mistral.invoke(messages)
    result = response.content
    print(f"ИИ(gpt_41): {result}")
    new_messages = state["messages"]+ [AIMessage(content = result)]

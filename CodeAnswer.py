from bundle import SystemState
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage, AIMessage
from config import llm_gpt_40

def codeAnswer(state: SystemState)->dict:
    user_input = state["current_message"]
    messages = [SystemMessage(content="Ты - программист с огромным стажем, дай краткий и информативный ответ")] + state["messages"]
    response = llm_gpt_40.invoke(messages)
    result = response.content
    print(f"ИИ(gpt_40): {result}")
    new_messages = state["messages"]+ [AIMessage(content = result)]
    return {
        "messages": new_messages,
        "code": result
    }

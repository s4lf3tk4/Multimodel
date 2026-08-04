from core import SystemState,analyzeDialog_parser, analyzeDialog_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from core import llm_gpt_54

def systematization(state: SystemState)->None:
    code = state.get("code", "")
    local = state.get("local", "")
    dialog = state.get("dialog", "")

    combined = ""
    if code:
        combined += f"Программирование: {code}\n"
    if local:
        combined += f"Локальные реалии: {local}\n"
    if dialog:
        combined += f"Общий диалог: {dialog}\n"

    if not combined:
        print("Нет данных для систематизации")


    analyzeDialog_chain = analyzeDialog_prompt | llm_gpt_54 | analyzeDialog_parser
    analyzeDialog_result = analyzeDialog_chain.invoke({"combined": combined})

    key_topics = analyzeDialog_result["key_topics"]
    summary = analyzeDialog_result["summary"]
    print(f"ИИ(gpt_51): Ключевые темы:{key_topics}\n Резюме: {summary}")

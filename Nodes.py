from bundle import SystemState, llm, classification_prompt, classification_parser
from langgraph.graph import StateGraph, START, END
from Routers import routerAfterInput, routerAfterClassification
from langchain_core.messages import HumanMessage
from CodeAnswer import codeAnswer
graph = StateGraph(SystemState)

@graph.add_node
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

@graph.add_node
def classifyMessage(state: SystemState)-> dict:
    user_input = state["current_message"]
    classification_chain = classification_prompt | llm | classification_parser
    classification_result = classification_chain.invoke({"user_input": user_input})

    message_type = classification_result["message_type"]
    confidence = classification_result["confidence"]

    print(f"Тип сообщения: {message_type}, уверенность: {confidence}")
    return{
        "message_type": message_type,
    }

@graph.add_node
def systematization(state: SystemState)->dict:
    if state["code"]:
        print(1)
    if state["dialog"]:
        print(2)
    if state["local"]:
        print(3)

graph.add_node("codeAnswer", codeAnswer)

graph.add_edge(START, "userInput")
graph.add_conditional_edges("userInput", routerAfterInput,{
    "input": "userInput",
    "classify": "classifyMessage"
})
graph.add_conditional_edges("classifyMessage", routerAfterClassification,{
    "code":"codeAnswer"
    # "dialog":"dialogAnswer",
    # "local":"localAnswer"
})
graph.add_edge("codeAnswer", END)

app = graph.compile()

initial_state = {
        "messages": [],
        "current_message": "",
        "message_type": "",
        "should_continue": True
    }
app.invoke(initial_state)

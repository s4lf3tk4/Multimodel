from langgraph.graph import StateGraph, START, END
from Nodes import userInput, classifyMessage, systematization
from Routers import routerAfterInput, routerAfterClassification
from CodeAnswer import codeAnswer
from dotenv import load_dotenv
from bundle import SystemState
import os
graph = StateGraph(SystemState)
graph.add_node("userInput", userInput)
graph.add_node("classifyMessage", classifyMessage)
graph.add_node("systematization", systematization)
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

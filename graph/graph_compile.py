from langgraph.graph import StateGraph, START, END
from graph.nodes import userInput, classifyMessage
from graph.routers import routerAfterInput, routerAfterClassification
from providers import codeAnswer
from providers import dialog
from providers import dialogOver
from providers import localDialog
from providers import systematization
from core import SystemState

graph = StateGraph(SystemState)

graph.add_node("userInput", userInput)
graph.add_node("classifyMessage", classifyMessage)
graph.add_node("systematization", systematization)
graph.add_node("dialogOver", dialogOver)
graph.add_node("codeAnswer", codeAnswer)
graph.add_node("dialog", dialog)
graph.add_node("localDialog", localDialog)

graph.add_edge(START, "userInput")
graph.add_conditional_edges("userInput", routerAfterInput,{
    "input": "userInput",
    "classify": "classifyMessage"
})
graph.add_conditional_edges("classifyMessage", routerAfterClassification,{
    "code":"codeAnswer",
    "dialog":"dialog",
    "local":"localDialog",
    "over": "dialogOver"
})
graph.add_edge("dialogOver", END)
graph.add_edge("codeAnswer", "systematization")
graph.add_edge("dialog", "systematization")
graph.add_edge("localDialog", "systematization")
graph.add_edge("systematization", "userInput")

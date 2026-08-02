from langgraph.graph import StateGraph, START, END
from Nodes import userInput, classifyMessage
from Routers import routerAfterInput, routerAfterClassification
from CodeAnswer import codeAnswer
from Dialog import dialog
from DialogOver import dialogOver
from LocalDialog import localDialog
from Systematization import systematization
from bundle import SystemState
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

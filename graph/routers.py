from core import SystemState

def routerAfterInput(state: SystemState)->str:
    current_message = state["current_message"]
    if not current_message:
        return "input"
    else:
        return "classify"

def routerAfterClassification(state: SystemState)-> str:
    message_type = state["message_type"]
    if message_type == "code":
        return "code"
    elif message_type == "local":
        return "local"
    elif message_type == "over":
        return "over"
    return "dialog"

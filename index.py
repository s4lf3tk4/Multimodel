from GraphCompile import graph


app = graph.compile()

initial_state = {
        "messages": [],
        "current_message": "",
        "message_type": "",
    }
app.invoke(initial_state)

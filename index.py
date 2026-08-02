from GraphCompile import graph

app = graph.compile()

initial_state = {
        "messages": [],
        "current_message": "",
        "message_type": "",
        "should_continue": True
    }
app.invoke(initial_state)

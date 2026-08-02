from GraphCompile import graph


app = graph.compile()

initial_state = {
        "messages": [],
        "current_message": "",
        "message_type": "",
    }


final_state = None
try:
    final_state = app.invoke(initial_state)
    print("-"*50)
    print(f"Чат завершен, сообщений: {len(final_state['messages'])}")
except KeyboardInterrupt:
        print("Чат прерван ctrl + c.")
except Exception as e:
     print(f"Ошибка в работае чата: {e}")

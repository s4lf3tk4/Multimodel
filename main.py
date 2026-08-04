from graph import graph
from core.settings import settings

app = graph.compile()

initial_state = {
        "messages": [],
        "current_message": "",
        "message_type": "",
    }

if settings.debug:
    import requests
    import json

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": "Привет", "stream": False},
            timeout=10
        )
        if response.status_code == 200:
            print("Ollama работает!")
            print(response.json()["response"])
        else:
            print(f"Ошибка: статус {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Исключение: {e}")

final_state = None
try:
    final_state = app.invoke(initial_state)
    print("-"*50)
    print(f"Чат завершен, сообщений: {len(final_state['messages'])}")
except KeyboardInterrupt:
        print("Чат прерван ctrl + c.")
except Exception as e:
     print(f"Ошибка в работае чата: {e}")

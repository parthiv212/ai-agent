from agent.graph import build_graph


def run():
    app = build_graph()

    state = {
        "user_input": "",
        "intent": None,
        "response": None,
        "name": None,
        "email": None,
        "platform": None,
        "stage": None,
        "lead_step": None,
    }

    print("\n🤖 AutoStream AI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        state["user_input"] = user_input

        result = app.invoke(state)

        print(f"Agent: {result['response']}\n")

        state.update(result)


if __name__ == "__main__":
    run()

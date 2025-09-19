from chatbot.agent import build_agent

def main():
    agent = build_agent()
    print("📚 Library Chatbot (Google PaLM/Gemini via LangChain). Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit","quit"}:
            break
        resp = agent.run(user_input)
        print("Bot:", resp)

if __name__ == "__main__":
    main()

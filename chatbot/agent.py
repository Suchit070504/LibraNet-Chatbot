# chatbot/agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from chatbot.tools import register_user, borrow_item, return_item, generate_reports, list_items

def build_agent():
    # model examples: "models/chat-bison-001" or other model ids (subject to availability)
    llm = ChatGoogleGenerativeAI(model="models/chat-bison-002", temperature=0)
    tools = [register_user, borrow_item, return_item, generate_reports, list_items]
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

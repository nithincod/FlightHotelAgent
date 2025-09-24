from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from tools.flights import flight_tool
from tools.hotels import hotel_tool
from llm_setup import get_llm

def create_travel_agent():
    llm = get_llm()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    tools = [flight_tool, hotel_tool]

    agent = initialize_agent(
        tools,
        llm,
        agent="chat-conversational-react-description",
        verbose=True,
        memory=memory
    )
    return agent

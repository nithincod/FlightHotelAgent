from agent import create_travel_agent

if __name__ == "__main__":
    print("=== Travel Assistant ===")
    agent = create_travel_agent()

    query = "I want to travel from New York to Los Angeles on 2025-10-10 and stay for 3 nights. Find me the cheapest flights and hotels."
    response = agent.run(query)

    print("\nAgent Response:\n", response)

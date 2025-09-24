from langchain.agents import Tool

def mock_flight_search(params):
    """
    Mock flight search (replace with real API call later).
    Expected input: {"origin": "NYC", "destination": "LAX", "date": "2025-10-10"}
    """
    origin = params.get("origin")
    destination = params.get("destination")
    date = params.get("date")
    
    return [
        {"airline": "Delta", "price": 250, "date": date, "route": f"{origin} → {destination}"},
        {"airline": "American Airlines", "price": 270, "date": date, "route": f"{origin} → {destination}"},
        {"airline": "United", "price": 300, "date": date, "route": f"{origin} → {destination}"}
    ]

flight_tool = Tool(
    name="Flight Search",
    func=mock_flight_search,
    description="Finds the cheapest flights. Input must be a dict: {origin, destination, date}"
)

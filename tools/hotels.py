from langchain.agents import Tool

def mock_hotel_search(params):
    """
    Mock hotel search (replace with Google Maps / Booking.com API later).
    Expected input: {"location": "Los Angeles", "checkin": "2025-10-10", "checkout": "2025-10-13"}
    """
    location = params.get("location")
    checkin = params.get("checkin")
    checkout = params.get("checkout")
    
    return [
        {"name": "Hotel California", "price": 120, "location": location, "dates": f"{checkin} to {checkout}"},
        {"name": "Sunset Inn", "price": 90, "location": location, "dates": f"{checkin} to {checkout}"},
        {"name": "Downtown Lodge", "price": 150, "location": location, "dates": f"{checkin} to {checkout}"}
    ]

hotel_tool = Tool(
    name="Hotel Search",
    func=mock_hotel_search,
    description="Finds affordable hotels. Input must be a dict: {location, checkin, checkout}"
)

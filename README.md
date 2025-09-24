# 🛫 Travel Assistant (LangChain Agent)

An autonomous **LangChain agent** that helps you find **cheap flights** and **affordable hotels**.  
Currently, it uses **mock APIs** for demonstration. Later, you can easily swap in real APIs like:  
- ✈️ **Skyscanner / Amadeus** for flights  
- 🏨 **Google Maps Places API / Booking.com** for hotels  

---

## 📂 Project Structure
```
travel_agent/
│── main.py              # Entry point
│── agent.py             # Initializes agent with tools + memory
│── llm_setup.py         # Configures free LLM (Groq / HuggingFace)
│── tools/
│     ├── flights.py     # Flight search tool (mocked)
│     ├── hotels.py      # Hotel search tool (mocked)
```

---

## 🚀 Features
- **LLM-powered reasoning** with LangChain agent  
- **Tool integration** (Flights + Hotels)  
- **Conversation memory** for personalized planning  
- **Mock API responses** (safe to test without real API keys)  
- **Easily extensible** → plug in real APIs later  

---

## ⚙️ Setup

### 1. Clone & Unzip
```bash
unzip travel_agent.zip
cd travel_agent
```

### 2. Install Dependencies
```bash
pip install langchain groq
```

*(Optional: add `requests` if you later replace mocks with real APIs.)*

### 3. Configure API Keys
For now, the agent uses **mock responses**, so you don’t need keys.  
But if you enable real APIs later:
- Get a **Groq API key** → [console.groq.com](https://console.groq.com/)  
- Replace `"YOUR_GROQ_API_KEY"` in `llm_setup.py`.  
- Add flight/hotel API keys inside `tools/flights.py` and `tools/hotels.py`.  

---

## ▶️ Run the Agent
```bash
python main.py
```

Example output:
```
=== Travel Assistant ===
> Entered new AgentExecutor chain...
Agent Response:
[{'airline': 'Delta', 'price': 250, 'date': '2025-10-10', 'route': 'NYC → LAX'},
 {'name': 'Hotel California', 'price': 120, 'location': 'Los Angeles', 'dates': '2025-10-10 to 2025-10-13'}]
```

---

## 🛠️ Requirements
- Python 3.9+  
- `langchain`  
- `groq`  

---

## 📌 Next Steps
- Add **real-time APIs** for production.  
- Build a **frontend (React/Flutter)** that calls this backend.  
- Deploy on **FastAPI/Flask** for serving responses.  

---



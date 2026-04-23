# 🤖 AutoStream Conversational AI Agent

A conversational AI agent built using LangGraph that handles user queries, detects intent, and captures leads for a fictional SaaS product (AutoStream).

---

## 🚀 Features

* Intent Detection (Greeting, Query, High Intent, Thank You)
* RAG-based response system (no LLM hallucination)
* Lead capture flow (Name → Email → Platform)
* Tool execution (mock CRM capture)
* Stateful conversation handling using LangGraph

---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/autostream-agent.git
cd autostream-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the agent

```bash
python main.py
```

---

## 🧠 Architecture Explanation

This project uses LangGraph to design a stateful conversational AI agent instead of a traditional stateless LLM pipeline.

LangGraph was chosen because it allows explicit control over conversation flow using nodes and edges, making it ideal for deterministic workflows like lead capture. Each node represents a function (intent classification, query handling, lead handling), and routing is controlled through conditional edges.

State is managed using a central `AgentState` object, which tracks user input, detected intent, responses, and lead collection progress (name, email, platform). This ensures continuity across multiple turns of conversation.

The system uses a lightweight RAG pipeline where responses are retrieved from a structured knowledge base (`knowledge.json`) instead of relying on an LLM. This prevents hallucination and ensures consistent answers.

When a high-intent signal is detected (e.g., "I want to buy"), the system transitions into a multi-step lead capture flow. This flow is controlled using `stage` and `lead_step` variables, ensuring the agent does not lose context.

A mock tool simulates CRM integration, demonstrating how real-world automation can be plugged into the system.

---

## 📲 WhatsApp Integration (Webhook Design)

To integrate this agent with WhatsApp:

1. Use WhatsApp Business API (via Meta or Twilio)
2. Set up a webhook endpoint (Flask/FastAPI server)
3. Incoming messages from WhatsApp → sent to your webhook
4. Extract user message → pass into LangGraph agent
5. Get agent response → send back via WhatsApp API

Flow:
User → WhatsApp → Webhook → Agent → Response → WhatsApp

You can maintain user sessions using phone numbers as unique IDs and store state in Redis or a database.

---

## 📁 Project Structure

```
autostream-agent/
│
├── main.py
├── requirements.txt
├── README.md
│
├── agent/
│   ├── graph.py
│   ├── state.py
│   ├── nodes.py
│   ├── intent.py
│   ├── rag.py
│   └── tools.py
│
└── data/
    └── knowledge.json
```

---

## ✅ Example Conversation

```
You: What are your pricing plans?
Agent: Here are our plans...

You: I want to buy
Agent: What's your name?

You: John
Agent: What's your email?

You: john@email.com
Agent: Which platform?

You: YouTube
Agent: Lead captured successfully 🎉
```

---

## Parhiv

Built as part of a GenAI assignment using LangGraph.

from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import (
    classify_intent,
    handle_greeting,
    handle_query,
    handle_lead,
    handle_thankyou
)


def route(state):
    # 🔴 If in lead stage → ALWAYS go to lead
    if state.get("stage") == "lead":
        return "lead"

    return state["intent"]


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", classify_intent)
    graph.add_node("greeting", handle_greeting)
    graph.add_node("query", handle_query)
    graph.add_node("lead", handle_lead)
    graph.add_node("thank_you", handle_thankyou)

    graph.set_entry_point("intent")

    graph.add_conditional_edges(
        "intent",
        route,
        {
            "greeting": "greeting",
            "query": "query",
            "high_intent": "lead",
            "lead": "lead",
            "thank_you": "thank_you"
        }
    )

    graph.add_edge("greeting", END)
    graph.add_edge("query", END)
    graph.add_edge("lead", END)
    graph.add_edge("thank_you", END)

    return graph.compile()

from agent.intent import detect_intent
from agent.rag import retrieve_answer
from agent.tools import mock_lead_capture


def classify_intent(state):
    # If already in lead flow → DO NOT reclassify
    if state.get("stage") == "lead":
        return state

    state["intent"] = detect_intent(state["user_input"])

    # If high intent → enter lead stage and set first step
    if state["intent"] == "high_intent":
        state["stage"] = "lead"
        state["lead_step"] = "ask_name"

    return state


def handle_greeting(state):
    state["response"] = (
        "👋 Hey there! Welcome to AutoStream — your video content automation platform. "
        "Feel free to ask about our plans, features, or how to get started!"
    )
    return state


def handle_query(state):
    state["response"] = retrieve_answer(state["user_input"])
    return state


def handle_thankyou(state):
    state["response"] = (
        "🙏 You're so welcome! It was a pleasure helping you. "
        "Wishing you all the best with your content journey. "
        "We're always here if you need anything!"
    )
    return state


def handle_lead(state):
    user_input = state["user_input"].strip()
    lead_step = state.get("lead_step", "ask_name")

    # Step 1: Ask for name
    if lead_step == "ask_name":
        state["response"] = "Great! I'd love to get you started. What's your name?"
        state["lead_step"] = "collect_name"
        return state

    # Step 2: Collect name, ask for email
    if lead_step == "collect_name":
        state["name"] = user_input
        state["response"] = f"Nice to meet you, {user_input}! What's your email address?"
        state["lead_step"] = "collect_email"
        return state

    # Step 3: Collect email, ask for platform
    if lead_step == "collect_email":
        state["email"] = user_input
        state["response"] = "Which platform do you create content on? (YouTube / Instagram)"
        state["lead_step"] = "collect_platform"
        return state

    # Step 4: Collect platform, complete lead capture
    if lead_step == "collect_platform":
        state["platform"] = user_input

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        state["response"] = (
            f"🎉 You're all set, {state['name']}! "
            "Our team will reach out to you soon. Is there anything else I can help you with?"
        )

        # Reset lead flow state
        state["stage"] = None
        state["lead_step"] = None

        return state

    return state

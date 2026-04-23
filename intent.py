def detect_intent(message: str) -> str:
    msg = message.lower()

    if any(x in msg for x in ["buy", "subscribe", "start", "sign up", "try"]):
        return "high_intent"

    elif any(x in msg for x in ["price", "pricing", "plan", "cost"]):
        return "query"

    elif any(x in msg for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in msg for x in ["thank you", "thanks", "thank u", "thx", "tysm", "ty"]):
        return "thank_you"

    return "query"

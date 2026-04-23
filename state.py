from typing import TypedDict, Optional


class AgentState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    stage: Optional[str]       # Tracks if we're in "lead" flow
    lead_step: Optional[str]   # Tracks exact step in lead flow:
   # "ask_name" → "collect_name" → "collect_email" → "collect_platform"

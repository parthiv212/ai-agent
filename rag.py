"""
rag.py — Rule-based retrieval for AutoStream Agent
All answers come directly from knowledge.json — no LLM involved.
"""

import json
import os

# Resolve knowledge.json path — tries data/ subfolder first, then project root
_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_kb_path = os.path.join(_root, "data", "knowledge.json")
if not os.path.exists(_kb_path):
    _kb_path = os.path.join(_root, "knowledge.json")

with open(_kb_path) as f:
    KB = json.load(f)


def retrieve_answer(query: str) -> str:
    q = query.lower()

    if any(x in q for x in ["price", "pricing", "plan", "cost"]):
        return (
            "Here are our plans:\n"
            f"  • Basic — {KB['pricing']['basic']['price']}: "
            f"{KB['pricing']['basic']['videos']}, {KB['pricing']['basic']['resolution']}\n"
            f"  • Pro   — {KB['pricing']['pro']['price']}: "
            f"{KB['pricing']['pro']['videos']}, {KB['pricing']['pro']['resolution']} + "
            f"{', '.join(KB['pricing']['pro']['features'])}"
        )

    if "refund" in q:
        return f"📋 Refund Policy: {KB['policies']['refund']}"

    if "support" in q:
        return f"🛠️ Support: {KB['policies']['support']}"

    # Generic fallback — no LLM
    return (
        "🤔 I'm not sure about that one. I can help you with:\n"
        "  • Pricing & plans\n"
        "  • Refund policy\n"
        "  • Support options\n"
        "  • Getting started / signing up\n"
        "What would you like to know?"
    )

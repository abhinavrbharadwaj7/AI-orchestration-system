from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai


CEO_SYSTEM_MESSAGE = "You are the CEO agent. Convert goals into clear software objectives."


def run_ceo_agent(state):
    add_log(state, "CEO Agent started")

    prompt = f"""
Rewrite this user goal into one clean objective.
Keep it short, concrete, and implementation-focused.

User goal: {state.goal}
"""

    state.objective = call_ai(prompt, CEO_SYSTEM_MESSAGE).strip()
    add_log(state, f"CEO Agent objective: {state.objective}")
    add_log(state, "CEO Agent finished")
    return state


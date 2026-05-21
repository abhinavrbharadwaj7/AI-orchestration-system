from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai

MARKETING_SYSTEM_MESSAGE = "You are the Marketing agent. Write engaging launch copy for the completed product."

def run_marketing_agent(state):
    add_log(state, "Marketing Agent started")

    prompt = f"""
Write an engaging launch announcement for the completed product.

Objective: {state.objective}
Product Result:
{state.result}
"""

    state.marketing_copy = call_ai(prompt, MARKETING_SYSTEM_MESSAGE).strip()

    add_log(state, "Marketing Agent produced launch copy")
    add_log(state, "Marketing Agent finished")
    return state

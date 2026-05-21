import json
from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai

PM_SYSTEM_MESSAGE = "You are the Product Manager agent. Break down the high-level objective into actionable product features."

def run_pm_agent(state):
    add_log(state, "PM Agent started")

    prompt = f"""
Break this objective into product features.
Return ONLY a JSON array of strings.
Do not include markdown.

Objective: {state.objective}
"""

    raw_features = call_ai(prompt, PM_SYSTEM_MESSAGE).strip()
    state.features = _parse_features(raw_features)

    add_log(state, f"PM Agent created {len(state.features)} feature(s)")
    for feature in state.features:
        add_log(state, f"Feature: {feature}")

    add_log(state, "PM Agent finished")
    return state

def _parse_features(raw_features: str) -> list[str]:
    try:
        parsed = json.loads(raw_features)
        if isinstance(parsed, list):
            return [str(f).strip() for f in parsed if str(f).strip()]
    except json.JSONDecodeError:
        pass

    return [line.strip("- ").strip() for line in raw_features.splitlines() if line.strip()]

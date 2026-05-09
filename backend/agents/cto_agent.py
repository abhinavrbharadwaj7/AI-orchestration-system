import json

from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai


CTO_SYSTEM_MESSAGE = "You are the CTO agent. Break objectives into simple implementation tasks."


def run_cto_agent(state):
    add_log(state, "CTO Agent started")

    prompt = f"""
Break this objective into implementation tasks.
Return ONLY a JSON array of strings.
Do not include markdown.

Objective: {state.objective}
"""

    raw_tasks = call_ai(prompt, CTO_SYSTEM_MESSAGE).strip()
    state.tasks = _parse_tasks(raw_tasks)

    add_log(state, f"CTO Agent created {len(state.tasks)} task(s)")
    for task in state.tasks:
        add_log(state, f"Task: {task}")

    add_log(state, "CTO Agent finished")
    return state


def _parse_tasks(raw_tasks: str) -> list[str]:
    try:
        parsed = json.loads(raw_tasks)
        if isinstance(parsed, list):
            return [str(task).strip() for task in parsed if str(task).strip()]
    except json.JSONDecodeError:
        pass

    return [line.strip("- ").strip() for line in raw_tasks.splitlines() if line.strip()]


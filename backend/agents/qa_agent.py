from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai


QA_SYSTEM_MESSAGE = "You are the QA agent. Validate output against the objective."
PASS_STATUS = "PASS"
FAIL_STATUS = "FAIL"


def run_qa_agent(state):
    add_log(state, "QA Agent started")

    prompt = f"""
Validate this generated result against the objective.
Return exactly one word: PASS or FAIL.

Objective: {state.objective}
Result:
{state.result}
"""

    raw_status = call_ai(prompt, QA_SYSTEM_MESSAGE).strip().upper()
    state.qa_status = PASS_STATUS if PASS_STATUS in raw_status else FAIL_STATUS

    add_log(state, f"QA Agent status: {state.qa_status}")
    add_log(state, "QA Agent finished")
    return state


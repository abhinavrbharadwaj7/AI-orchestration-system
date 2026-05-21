from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai


QA_SYSTEM_MESSAGE = "You are the QA agent. Validate output against the objective."
PASS_STATUS = "PASS"
FAIL_STATUS = "FAIL"


def run_qa_agent(state):
    add_log(state, "QA Agent started")

    prompt = f"""
Validate this generated result against the objective.
Analyze the result carefully to ensure it fully meets the objective.
If the result successfully achieves the objective, return exactly one word: PASS.
If the result fails to meet the objective in any way, return FAIL on the first line.
On the subsequent lines, provide a clear, detailed explanation of exactly why it failed, what is missing or incorrect, and actionable steps to fix it.

Objective: {state.objective}
Result:
{state.result}
"""

    response = call_ai(prompt, QA_SYSTEM_MESSAGE).strip()

    if response.upper().startswith(PASS_STATUS):
        state.qa_status = PASS_STATUS
        state.qa_feedback = ""
    else:
        state.qa_status = FAIL_STATUS
        # Extract feedback if available (everything after the first line)
        parts = response.split('\n', 1)
        if len(parts) > 1:
            state.qa_feedback = parts[1].strip()
        else:
            state.qa_feedback = response

    add_log(state, f"QA Agent status: {state.qa_status}")
    if state.qa_feedback:
        add_log(state, f"QA Agent feedback: {state.qa_feedback}")
    add_log(state, "QA Agent finished")
    return state


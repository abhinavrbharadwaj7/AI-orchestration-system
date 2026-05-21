from backend.orchestrator.logger import add_log
from backend.services.ai_service import call_ai


DEV_SYSTEM_MESSAGE = "You are the Dev agent. Execute tasks and produce the requested output."


def run_dev_agent(state):
    add_log(state, "Dev Agent started")

    task_list = "\n".join(f"- {task}" for task in state.tasks)

    feedback_section = ""
    if state.retry_count > 0 and state.qa_feedback:
        feedback_section = f"""
Previous attempt failed QA. Please address the following feedback in your new result:
QA Feedback:
{state.qa_feedback}

Previous Result:
{state.result}
"""

    prompt = f"""
Execute these implementation tasks and produce the best possible result.
Return only the final generated output.

Objective: {state.objective}
Retry count: {state.retry_count}
Tasks:
{task_list}
{feedback_section}
"""

    state.result = call_ai(prompt, DEV_SYSTEM_MESSAGE).strip()
    add_log(state, "Dev Agent produced result")
    add_log(state, "Dev Agent finished")
    return state


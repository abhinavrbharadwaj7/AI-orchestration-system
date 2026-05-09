from backend.agents.ceo_agent import run_ceo_agent
from backend.agents.cto_agent import run_cto_agent
from backend.agents.dev_agent import run_dev_agent
from backend.agents.qa_agent import PASS_STATUS, run_qa_agent
from backend.orchestrator.logger import add_log
from backend.orchestrator.state import create_initial_state


MAX_RETRY_COUNT = 3


def run_orchestrator(goal: str):
    state = create_initial_state(goal)

    add_log(state, "Orchestrator started")
    add_log(state, f"User goal: {state.goal}")

    state = run_ceo_agent(state)
    state = run_cto_agent(state)

    while state.retry_count < MAX_RETRY_COUNT:
        state = run_dev_agent(state)
        state = run_qa_agent(state)

        if state.qa_status == PASS_STATUS:
            add_log(state, "QA passed. Orchestrator finished successfully")
            return state

        state.retry_count += 1
        add_log(state, f"QA failed. Retrying Dev Agent ({state.retry_count}/{MAX_RETRY_COUNT})")

    add_log(state, "Maximum retries reached. Orchestrator finished with QA failure")
    return state


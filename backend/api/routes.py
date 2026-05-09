from fastapi import APIRouter, HTTPException, Query

from backend.orchestrator.orchestrator import run_orchestrator


MIN_GOAL_LENGTH = 3

router = APIRouter()


@router.get("/run")
def run(goal: str = Query(..., min_length=MIN_GOAL_LENGTH)):
    clean_goal = goal.strip()

    if len(clean_goal) < MIN_GOAL_LENGTH:
        raise HTTPException(status_code=400, detail="Goal is too short.")

    state = run_orchestrator(clean_goal)
    return state.to_dict()


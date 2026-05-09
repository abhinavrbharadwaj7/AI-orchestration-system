import sys

from backend.orchestrator.orchestrator import run_orchestrator


DEFAULT_GOAL = "Create a Python function that adds two numbers."


def main():
    goal = " ".join(sys.argv[1:]).strip() or DEFAULT_GOAL
    state = run_orchestrator(goal)

    print("\nFinal State")
    print("===========")
    print(state.to_dict())


if __name__ == "__main__":
    main()

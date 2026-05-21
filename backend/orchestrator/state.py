from dataclasses import dataclass, field


@dataclass
class OrchestratorState:
    goal: str = ""
    objective: str = ""
    tasks: list[str] = field(default_factory=list)
    result: str = ""
    qa_status: str = ""
    qa_feedback: str = ""
    retry_count: int = 0
    logs: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "goal": self.goal,
            "objective": self.objective,
            "tasks": self.tasks,
            "result": self.result,
            "qa_status": self.qa_status,
            "qa_feedback": self.qa_feedback,
            "retry_count": self.retry_count,
            "logs": self.logs,
        }


def create_initial_state(goal: str) -> OrchestratorState:
    return OrchestratorState(goal=goal.strip())


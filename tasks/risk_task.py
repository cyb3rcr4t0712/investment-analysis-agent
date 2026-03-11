from crewai import Task
from agents.risk_evaluator import risk_evaluator


def create_risk_task(company: str) -> Task:
    """Create a risk evaluation task for the given company."""
    return Task(
        description=(
            f"Identify and evaluate the market, operational, legal, and "
            f"regulatory risks associated with {company}."
        ),
        expected_output=(
            f"A comprehensive summary of potential risks for {company} and their "
            "possible impact on the investment."
        ),
        agent=risk_evaluator,
        context=[]
    )
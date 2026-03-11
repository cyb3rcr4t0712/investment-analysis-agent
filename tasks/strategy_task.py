from crewai import Task
from agents.strategy_recommender import strategy_recommender


def create_strategy_task(company: str, context: list = None) -> Task:
    """Create a strategy recommendation task for the given company."""
    return Task(
        description=(
            f"Combine all provided reports to give a Buy/Sell/Hold recommendation "
            f"for {company} with reasons. Evaluate it based on the combined findings."
        ),
        expected_output=(
            f"A final recommendation (Buy/Sell/Hold) for {company}, a summary of "
            "the key reasons, and two important disclaimers for the investment."
        ),
        agent=strategy_recommender,
        context=context or []
    )
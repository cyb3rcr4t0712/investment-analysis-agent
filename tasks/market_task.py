from crewai import Task
from agents.market_analyst import market_analyst


def create_market_task(company: str) -> Task:
    """Create a market analysis task for the given company."""
    return Task(
        description=(
            f"Analyze the latest market trends, competitive landscape, and economic "
            f"indicators relevant to {company}. Focus on the last quarter."
        ),
        expected_output=(
            f"A concise report on market conditions around {company}, competitor "
            "performance, and overall industry sentiment."
        ),
        agent=market_analyst,
        context=[]
    )
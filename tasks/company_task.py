from crewai import Task
from agents.company_analyst import company_analyst


def create_company_task(company: str) -> Task:
    """Create a company analysis task for the given company."""
    return Task(
        description=(
            f"Conduct a thorough analysis of {company}'s financial health. "
            "Look at revenue growth, profit margins, and key performance metrics "
            "from recent earnings reports."
        ),
        expected_output=(
            f"A detailed report on {company}'s financial stability, growth "
            "prospects, and recent developments."
        ),
        agent=company_analyst,
        context=[]
    )
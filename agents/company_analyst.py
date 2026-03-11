from crewai import Agent
from crewai_tools import DuckDuckGoSearchRun

# Initialize the search tool
search_tool = DuckDuckGoSearchRun()

# Define the Company Analyst Agent
company_analyst = Agent(
    role='Corporate Financial Analyst',
    goal='Quantify the financial health and performance of the target company by analyzing its financial statements, revenue growth, and key performance metrics.',
    backstory=(
        'You are a detail-oriented Financial Analyst who lives and breathes financial statements. '
        'Your mission is to look beyond the surface-level numbers to reveal the true financial '
        'story of a company.'
    ),
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)
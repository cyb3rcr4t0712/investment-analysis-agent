from crewai import Agent
from crewai_tools import DuckDuckGoSearchRun

# Initialize the search tool
search_tool = DuckDuckGoSearchRun()

# Define the Market Analyst Agent
market_analyst = Agent(
    role='Lead Market Analyst',
    goal='Uncover and report on the latest market trends, competitive landscape, and economic indicators impacting the target company.',
    backstory=(
        'You are a seasoned Market Analyst with a keen eye for dissecting market dynamics. '
        'You are known for your ability to find the signal in the noise and provide clear, '
        'actionable insights from complex data.'
    ),
    verbose=True,
    allow_delegation=False,
    # Add the tool to the agent
    tools=[search_tool]
)
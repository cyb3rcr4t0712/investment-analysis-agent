from crewai import Agent
from crewai_tools import DuckDuckGoSearchRun

# Initialize the search tool
search_tool = DuckDuckGoSearchRun()

# Define the Investment Strategist Agent
strategy_recommender = Agent(
    role='Chief Investment Strategist',
    goal='Synthesize all provided analyses into a single, comprehensive investment thesis and provide a clear "Buy," "Sell," or "Hold" recommendation.',
    backstory=(
        'You are the Chief Investment Strategist, a veteran of market cycles. Your judgment is '
        'trusted because you weigh all evidence—market trends, financial health, and potential '
        'risks—to craft a balanced and decisive final recommendation.'
    ),
    verbose=True,
    allow_delegation=False,
    # Add the tool to the agent
    tools=[search_tool]
)
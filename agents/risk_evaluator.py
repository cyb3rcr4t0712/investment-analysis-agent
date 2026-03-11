from crewai import Agent
from crewai_tools import DuckDuckGoSearchRun

# Initialize the search tool
search_tool = DuckDuckGoSearchRun()

# Define the Risk Evaluator Agent
risk_evaluator = Agent(
    role='Risk Assessment Specialist',
    goal='Identify, evaluate, and report on the full spectrum of market, operational, legal, and regulatory risks associated with the target company.',
    backstory=(
        'You are a pragmatic Risk Assessment Specialist with a knack for seeing around corners. '
        'Your job is to anticipate potential threats and provide a clear-eyed view of the challenges '
        'an investment might face.'
    ),
    verbose=True,
    allow_delegation=False,
    # Add the tool to the agent
    tools=[search_tool]
)
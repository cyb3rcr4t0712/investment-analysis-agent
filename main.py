import os
from dotenv import load_dotenv
from fi_instrumentation import register
from fi_instrumentation.fi_types import ProjectType
from traceai_crewai import CrewAIInstrumentor

# --- Load API Keys from .env file ---
load_dotenv()

# --- FutureAGI Tracing Setup ---
trace_provider = register(
    project_type=ProjectType.OBSERVE,
    project_name="crewai_project"
)
CrewAIInstrumentor().instrument(tracer_provider=trace_provider)

# --- Get Target Company ---
company = input("Enter the company name to analyze (e.g., Tesla, Apple): ").strip()
if not company:
    print("No company name provided. Exiting.")
    exit(1)

# --- Import Agents & Tasks ---
from agents.market_analyst import market_analyst
from agents.company_analyst import company_analyst
from agents.risk_evaluator import risk_evaluator
from agents.strategy_recommender import strategy_recommender

from tasks.market_task import create_market_task
from tasks.company_task import create_company_task
from tasks.risk_task import create_risk_task
from tasks.strategy_task import create_strategy_task

# --- Create Tasks with the Target Company ---
task_market = create_market_task(company)
task_company = create_company_task(company)
task_risk = create_risk_task(company)
task_strategy = create_strategy_task(company, context=[task_market, task_company, task_risk])

from crewai import Crew, Process

# --- Assemble the Crew ---
crew = Crew(
    agents=[
        market_analyst,
        company_analyst,
        risk_evaluator,
        strategy_recommender
    ],
    tasks=[
        task_market,
        task_company,
        task_risk,
        task_strategy
    ],
    process=Process.sequential,
    verbose=True
)

# --- Run the Crew ---
print(f"\n🚀 Kicking off analysis for {company}...")
results = crew.kickoff()

# --- Print the Final Results ---
print("\n\n--- Final Recommendation ---")
print(results)
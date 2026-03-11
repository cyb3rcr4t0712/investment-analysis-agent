# Investment Analysis Agent

A multi-agent investment research tool built with [CrewAI](https://github.com/joaomdmoura/crewai) and traced with [FutureAGI](https://futureagi.com). Given a company name, four specialized AI agents work sequentially to produce a final Buy/Sell/Hold recommendation.

---

## Agents

| Agent | Role |
|---|---|
| Market Analyst | Analyzes market trends, competitors, and economic indicators |
| Company Analyst | Evaluates financial health, revenue growth, and key metrics |
| Risk Evaluator | Identifies market, operational, legal, and regulatory risks |
| Strategy Recommender | Synthesizes all reports into a final investment recommendation |

---

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key
- A FutureAGI account (for tracing)

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/investment-analysis-agent.git
   cd investment-analysis-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by copying the example file:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and fill in your API keys:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   FI_API_KEY=your-fi-api-key-here
   FI_SECRET_KEY=your-fi-secret-key-here
   ```

---

## Usage

```bash
python main.py
```

You will be prompted to enter the company name you want to analyze:

```
Enter the company name to analyze (e.g., Tesla, Apple): Nvidia
```

The four agents will run sequentially and print a final recommendation when complete.

---

## Project Structure

```
.
+-- main.py                  # Entry point
+-- requirements.txt
+-- .env.example             # Template for environment variables
+-- agents/
|   +-- company_analyst.py
|   +-- market_analyst.py
|   +-- risk_evaluator.py
|   +-- strategy_recommender.py
+-- tasks/
    +-- company_task.py
    +-- market_task.py
    +-- risk_task.py
    +-- strategy_task.py
```

---

## Tracing

All agent runs are traced via FutureAGI's instrumentation. After running, view your traces in the FutureAGI dashboard under the project name `crewai_project`.

---

## Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `FI_API_KEY` | Your FutureAGI API key |
| `FI_SECRET_KEY` | Your FutureAGI secret key |

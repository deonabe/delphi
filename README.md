# 🧠 Delphi: A Crypto Reasoning Agent

---

## 📌 Project Purpose & Summary

**Delphi** is an experimental crypto research tool that simulates how a human analyst might reason through market data and narrative sentiment to arrive at a trading decision.

Rather than treat trading as a black-box prediction problem, Delphi breaks down the process into interpretable steps. Inspired by how analysts at firms like **Messari**, **Arkham**, and **Galaxy Research** work, Delphi models the research pipeline using modular **LLM agents** — each responsible for a distinct layer of reasoning:

* 📊 Extracting objective facts from price and news data
* 🧠 Separating speculation from truth
* 💭 Formulating a research-backed trade thesis
* 🧾 Outputting a fully explainable buy/sell/wait recommendation

The result is a system that doesn’t just say “buy” or “sell,” but **shows its work** — just like a real analyst would in a coverage report.

---

## 🧠 Inspiration

This project draws from several trends and needs across the crypto and AI research space:

* The rise of **LLM agent frameworks** (e.g., AutoGPT, LangChain, CrewAI)
* The challenge of separating **narrative from data** in volatile markets
* The vision of human-like reasoning in papers like
  *“Exploring LLM Cryptocurrency Trading Through Fact-Subjectivity Aware Reasoning”* (2024)
* The need for **transparent, explainable, data-driven tools** for DeFi investors, analysts, and protocol researchers

---

## 🎯 Vision

Delphi aims to emulate the workflow of a seasoned crypto analyst by building a pipeline that:

1. **Ingests** real-world price data and news
2. **Extracts** objective facts from those inputs
3. **Identifies** speculative or subjective sentiment
4. **Constructs** a trade rationale based on signals
5. **Outputs** an interpretable recommendation with supporting rationale

In short:

> “What would Messari’s analyst say today — and why?”

---

## 🧱 Architecture Overview (MVP)

```
[ Price Data + News Headlines ] ──▶ 🧠 Fact Agent
                                       │
                                       ▼
                             🧠 Subjectivity Agent
                                       │
                                       ▼
                              🧠 Strategy Agent
                                       │
                                       ▼
                       ✅ Trade Action + Explanation
```

Each component is modular and swappable, allowing for experimentation with different models, heuristics, and data sources.

---

## ✅ Completed So Far (Week 1)

### 1. Project Structure

* Created a clean, modular directory layout:

```
/data/raw/         ← raw ETH price data and simulated news  
/data/processed/   ← merged and agent-ready daily records  
/scripts/          ← data fetchers and agent runners  
/agents/           ← LLM prompt templates and logic  
```

This structure ensures separation of concerns and easy extension as the agent pipeline grows.

---

### 2. ETH Price Data Pipeline

* Used the **CoinGecko Pro API** to fetch \~1 year of daily ETH data:

  * `price`
  * `market_cap`
  * `24h volume`

* Navigated API constraints (e.g., 365-day window, granularity issues)

* Converted UNIX timestamps to date strings

* Exported and validated output in `data/processed/eth_2024_2025.csv`

---

### 3. ETH News Simulation

* Built a generator for **realistic, time-aligned crypto headlines**

* Categories include:

  * Regulatory actions
  * Exchange outages
  * Token unlocks
  * ETH ETF rumors
  * On-chain hacks

* Outputs \~3 headlines/day to simulate the **narrative noise** an analyst would see

* Stored as JSONL in `data/processed/eth_news_2024_2025.jsonl`

This step bootstraps the "market sentiment" layer that Delphi’s reasoning agents can interpret.

---

### 4. Price + News Merge

* Created a script to merge price and news by date
* Output format for each day:

```json
{
  "date": "2024-08-01",
  "price_data": {
    "price": 3233.08,
    "volume": 16143420325.48,
    "market_cap": 388633791826.87
  },
  "headlines": [
    "Ethereum surges after ETF rumors gain traction",
    "Binance temporarily pauses ETH withdrawals due to traffic"
  ]
}
```

* Final file: `data/processed/eth_merged_2024_2025.jsonl`
  → This becomes the **input to the Fact Agent**

---

### 5. Fact Agent Prompt + Infrastructure

The **Fact Agent** is Delphi’s first reasoning module. It processes one day of ETH data and headlines, and extracts **objective facts** — the “what happened,” not the “why” or “what it means.”

#### What It Does:

* Reads daily ETH price + news data
* Extracts 2–4 bullet-point facts (e.g., price movement, events, protocol changes)
* Ignores speculation or narrative framing

#### Built:

* A reusable **prompt template** in `agents/fact_agent_template.txt`
* A script to render and send prompts: `scripts/run_fact_agent.py`
* Fact output saved to `data/processed/eth_facts_2024_2025.jsonl`

#### Example Output:

```json
{
  "date": "2024-08-01",
  "facts": [
    "ETH price closed at $3233.08.",
    "Binance paused ETH withdrawals due to high traffic.",
    "Ethereum saw trading volume over $16B."
  ]
}
```

> ⚠️ Currently waiting on OpenAI billing setup to complete full run.
> A **mock agent** is available to simulate responses if needed.

---

## 🔜 Next Steps

* ✅ Run the Fact Agent across full dataset (after billing enabled)
* 🧠 Build the **Subjectivity Agent** to extract speculation, framing, and opinions
* 🪜 Chain agents together into a full pipeline
* 📈 Visualize daily trade theses and outcomes
* 🎯 Explore basic **strategy simulation** (backtest thesis-led trading)

-

## 🗂️ Delphi /data/ Directory

This directory contains all datasets used in Delphi’s reasoning pipeline. It’s organized into two subfolders:

---

### 📁 `raw/`

This folder holds unprocessed source data, either fetched via API or generated for simulation.

**Contents:**

| File                       | Description                                                        |
| -------------------------- | ------------------------------------------------------------------ |
| `eth_2024_2025.csv`        | Daily ETH price, volume, and market cap from CoinGecko             |
| `eth_news_2024_2025.jsonl` | Simulated headlines (\~3 per day) aligned with each ETH price date |

---

### 📁 `processed/`

This folder contains data that’s been cleaned, merged, or transformed for use in the LLM agent pipeline.

**Contents:**

| File                               | Description                                                       |
| ---------------------------------- | ----------------------------------------------------------------- |
| `eth_merged_2024_2025.jsonl`       | Each entry contains ETH price data + headlines for a specific day |
| `eth_facts_2024_2025.jsonl`        | Output of the Fact Agent (objective, extracted facts per day)     |
| `eth_subjectivity_2024_2025.jsonl` | *(planned)* Output of Subjectivity Agent (opinions/speculation)   |
| `eth_theses_2024_2025.jsonl`       | *(planned)* Strategy Agent output (trade rationale + action)      |

---

### 🔄 Workflow Summary

1. **Fetch price data** → save to `/raw/eth_2024_2025.csv`
2. **Generate headlines** → save to `/raw/eth_news_2024_2025.jsonl`
3. **Merge into daily records** → output `/processed/eth_merged_2024_2025.jsonl`
4. **Run agents** (Fact → Subjectivity → Strategy)
5. Each agent appends new files to `/processed/`

---

### 📌 Notes

* All files are aligned by `"date"` in ISO format (YYYY-MM-DD)
* Use `.jsonl` format for streaming and line-by-line LLM processing
* The `processed/` folder reflects **state after each agent runs**


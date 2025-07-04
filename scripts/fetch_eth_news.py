# scripts/generate_mock_eth_news.py

import json
import random
from pathlib import Path

import pandas as pd

# Load ETH price data to match the date range
price_df = pd.read_csv("data/raw/prices/eth_2024_2025.csv")
dates = pd.to_datetime(price_df["date"]).dt.date

# Choose a smaller subset to simulate (e.g. first 30 days)
mock_dates = dates[:30]

# Mock headline templates
headline_templates = [
    "Ethereum price surges after {event}",
    "Vitalik Buterin comments on {topic}",
    "SEC discusses regulations on {subject}",
    "ETH gas fees {action} as usage spikes",
    "{company} announces support for Ethereum staking",
    "Analysts debate {debate}",
    "Layer 2 networks like {layer2} gain traction",
    "{protocol} TVL crosses new milestone",
    "Ethereum developers push upgrade: {upgrade_name}",
    "Market reacts to {market_event}",
]

# Some fill-in values
event_keywords = [
    "BlackRock filing",
    "tokenization boom",
    "Layer 2 rollout",
    "Shanghai upgrade",
    "ETF rumor",
    "stablecoin adoption",
    "DeFi rebound",
    "macro headwinds",
]
topics = ["scalability", "security", "governance", "layer 3 solutions"]
subjects = ["crypto exchanges", "staking platforms", "Ethereum ETFs"]
actions = ["drop", "increase", "stabilize", "skyrocket"]
companies = ["Coinbase", "Binance", "Kraken", "PayPal"]
debates = [
    "Ethereum inflation vs. deflation",
    "ETH as a store of value",
    "staking centralization",
]
layer2s = ["Arbitrum", "Optimism", "Base", "zkSync"]
protocols = ["Uniswap", "Aave", "Lido", "Curve"]
upgrades = ["Pectra", "Verkle Trees", "Account Abstraction"]
market_events = ["rate hike fears", "market volatility", "Bitcoin halving anticipation"]

# Output path
out_path = Path("data/raw/news/eth_news_2024_2025.jsonl")
out_path.parent.mkdir(parents=True, exist_ok=True)

# Generate and write mock headlines
with open(out_path, "w") as f:
    for date in mock_dates:
        headlines = []
        for _ in range(random.randint(2, 4)):  # 2–4 headlines per day
            template = random.choice(headline_templates)
            headline = template.format(
                event=random.choice(event_keywords),
                topic=random.choice(topics),
                subject=random.choice(subjects),
                action=random.choice(actions),
                company=random.choice(companies),
                debate=random.choice(debates),
                layer2=random.choice(layer2s),
                protocol=random.choice(protocols),
                upgrade_name=random.choice(upgrades),
                market_event=random.choice(market_events),
            )
            headlines.append(headline)

        json.dump({"date": str(date), "headlines": headlines}, f)
        f.write("\n")

print("✅ Mock ETH news saved to:", out_path)

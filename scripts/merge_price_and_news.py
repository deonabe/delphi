import json
from datetime import datetime
from pathlib import Path

import pandas as pd

# Paths
price_path = Path("data/raw/prices/eth_2024_2025.csv")
news_path = Path("data/raw/news/eth_news_2024_2025.jsonl")
output_path = Path("data/processed/eth_merged_2024_2025.jsonl")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Load ETH price data
price_df = pd.read_csv(price_path)
price_df["date"] = pd.to_datetime(price_df["date"]).dt.date
price_map = {
    row.date: {
        "price": round(row.price, 2),
        "volume": round(row.volume, 2),
        "market_cap": round(row.market_cap, 2),
    }
    for row in price_df.itertuples()
}

# Load news headlines
news_map = {}
with open(news_path, "r") as f:
    for line in f:
        item = json.loads(line)
        date_obj = datetime.strptime(item["date"], "%Y-%m-%d").date()
        news_map[date_obj] = item["headlines"]

# Merge into daily reasoning entries
with open(output_path, "w") as out_file:
    for date in sorted(price_map):
        if date in news_map:
            combined_entry = {
                "date": str(date),
                "price_data": price_map[date],
                "headlines": news_map[date],
            }
            json.dump(combined_entry, out_file)
            out_file.write("\n")
            print(f"✅ {date}: merged")
        else:
            print(f"⚠️ {date}: no headlines found")

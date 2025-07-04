# scripts/fetch_eth_price.py

import pandas as pd
import requests

# Date range: Jan 1 – Mar 31, 2023 (UNIX timestamps in seconds)
from_ts = 1722384000  # 2023-01-01
to_ts = 1753920000  # 2023-03-31

url = (
    f"https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range"
    f"?vs_currency=usd&from={from_ts}&to={to_ts}"
)

response = requests.get(url)
data = response.json()

# print("Status code:", response.status_code)

# Parse price data (timestamp, price)
prices = data["prices"]
market_caps = data["market_caps"]
volumes = data["total_volumes"]

# Convert to DataFrames
df_price = pd.DataFrame(prices, columns=["timestamp", "price"])
df_price["date"] = pd.to_datetime(df_price["timestamp"], unit="ms").dt.date

df_volume = pd.DataFrame(volumes, columns=["timestamp", "volume"])
df_volume["date"] = pd.to_datetime(df_volume["timestamp"], unit="ms").dt.date

df_cap = pd.DataFrame(market_caps, columns=["timestamp", "market_cap"])
df_cap["date"] = pd.to_datetime(df_cap["timestamp"], unit="ms").dt.date

# Merge on date and drop duplicates (keep first per day)
df = (
    df_price[["date", "price"]]
    .merge(df_volume[["date", "volume"]], on="date")
    .merge(df_cap[["date", "market_cap"]], on="date")
    .drop_duplicates(subset=["date"])
)

# Sort and save
df = df.sort_values("date")
df.to_csv("data/raw/prices/eth_2024_2025.csv", index=False)

print("✅ ETH price data saved!")

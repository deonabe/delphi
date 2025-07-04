import json
import os
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Template
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
models = client.models.list()
print([m.id for m in models.data])

# Paths
input_path = Path("data/processed/eth_merged_2024_2025.jsonl")
output_path = Path("data/processed/eth_facts_2024_2025.jsonl")
template_path = Path("agents/fact_agent_template.txt")

# Load template
with open(template_path, "r") as f:
    template = Template(f.read())

# Load input data
with open(input_path, "r") as f:
    entries = [json.loads(line) for line in f]

# How many days to process for testing
N = 5

# Process and save
with open(output_path, "w") as out_file:
    for entry in entries[:N]:
        rendered_prompt = template.render(
            price=entry["price_data"]["price"],
            volume=entry["price_data"]["volume"],
            market_cap=entry["price_data"]["market_cap"],
            headlines=entry["headlines"],
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a crypto research assistant.",
                    },
                    {"role": "user", "content": rendered_prompt},
                ],
                temperature=0.3,
            )

            facts = response.choices[0].message.content.strip()

            # Save response
            json.dump(
                {
                    "date": entry["date"],
                    "facts": json.loads(facts) if facts.startswith("[") else [facts],
                },
                out_file,
            )
            out_file.write("\n")

            print(f"✅ {entry['date']}: extracted {len(json.loads(facts))} facts")

        except Exception as e:
            print(f"⚠️ Error on {entry['date']}: {e}")

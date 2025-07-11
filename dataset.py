import pandas as pd
import json

with open(r"E:\\DA\\deloitte\\daikibo-telemetry-data.json", encoding='utf-8') as f:  
    data = json.load(f)

print("✅ Loaded JSON:")
print(data[:2])  # See the first two entries (if it’s a list)

df = pd.json_normalize(data)
print("✅ DataFrame shape:", df.shape)  # Check if it’s empty

df.to_csv("flattened_data.csv", index=False)

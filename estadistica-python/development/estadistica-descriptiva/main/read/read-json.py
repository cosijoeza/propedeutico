# Read json file.
import pandas as pd

# Read file.
df_json = pd.read_json("files/example_json.json")

# Show first rows.
print(df_json.head())
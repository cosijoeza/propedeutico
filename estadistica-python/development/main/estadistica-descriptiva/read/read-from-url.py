# Read file from url.

import pandas as pd

# Read file.
df_url = pd.read_csv("https://example.com/data.csv")

# Show first rows.
print(df_url.head())
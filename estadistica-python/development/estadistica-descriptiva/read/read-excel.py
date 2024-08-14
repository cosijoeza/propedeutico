# Read excel file.
import pandas as pd

# Load file.
df_excel = pd.read_excel("files/example_excel.xlsx")

# Show first rows.
print(df_excel.head())
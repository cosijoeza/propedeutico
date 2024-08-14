# Read from SQL.
import pandas as pd
from sqlalchemy import engine

# Connect with sql.
engine = create_engine("SQLpath")

# Read a table.
df_sql = pd.read_sql_table("table_name",engine)

# Show first rows.
print(df_sql.head())
# Range and Interquartile range.
# Leasson 5.
import pandas as pd

# Simulacion de datos de evaluaciones
data = {
    'satisfaction':[4,5,5,6,7,7,8,9,2,10,5,6,7,8,9,4,4,5,6,7]
}

# Set into dataframe.
df = pd.DataFrame(data)

# Get range.
data_range = df['satisfaction'].max() - df['satisfaction'].min()

print("Maximun: ",df['satisfaction'].max())
print("Minimum: ",df['satisfaction'].min())
print("Satisfaction range: ", data_range)

# Get interquartile range.
q1 = df['satisfaction'].quantile(q=0.25)
q3 = df['satisfaction'].quantile(q=0.75)
iqr = q3 - q1

print("Interquartile Range Q1:",q1)
print("Interquartile Range Q3:",q3)
print("Satisfaction Interquartile Range: ",iqr)
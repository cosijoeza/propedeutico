# LIKERT SCALE - GRAFICO DE BARRAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Answers simulation.
np.random.seed(42)

satisfaction_data = np.random.choice(
    a=[
        "1.-Muy Insatisfecho",
        "2.-Insatisfecho",
        "3.-Neutral",
        "4.-Satisfecho",
        "5.-Muy Satisfecho",
    ],
    size=300,
    p=[0.05, 0.15, 0.20, 0.40, 0.20],
)

# Create dataframe.
df = pd.DataFrame(satisfaction_data, columns=["Satisfaccion"])

# Create frecuency tables.
frecuency_table = df["Satisfaccion"].value_counts().sort_index()

# Graphics configuration and create bar graph.
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10,6))
sns.barplot(x = frecuency_table.index,y=frecuency_table.values,palette='Blues_d')
plt.title('Frecuencia de satisfaccion de servicios de biblioteca')
plt.xlabel('Nivel de satisfaccion')
plt.ylabel('Frecuencia')
plt.show()

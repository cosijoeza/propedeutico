# LIKERT SCALE - HISTOGRAMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data simulation.
np.random.seed(42)
sampleSize = 1000

# Mean = 50, desviation standar = 10
score = np.random.normal(loc=50, scale=10, size=sampleSize)

# Likert scale data simulation.
socioeconomicLevel = np.random.choice(
    a=["Bajo", "Medio", "Alto"], size=sampleSize, p=[0.4, 0.4, 0.2]
)

# Set dataframe.
df = pd.DataFrame({"Puntuaciones": score, "NSE": socioeconomicLevel})

# Adjust scores to reflect possible bias socioeconomic.
adjustmentBias = {"Bajo": -5, "Medio": 0, "Alto": 5}

df["PuntuacionesAjustadas"] = df.apply(
    lambda x: x["Puntuaciones"] + adjustmentBias[x["NSE"]], axis=1
)

# Configure visualization.
sns.set_theme(style="darkgrid")

# Create histogram.
plt.figure(figsize=(14, 7))
for i, sel in enumerate(["Bajo", "Medio", "Alto"], 1):
    plt.subplot(1, 3, i)
    subset = df[df["NSE"] == sel]
    sns.histplot(
        subset["PuntuacionesAjustadas"],
        kde=False,
        bins=30,
        color="skyblue",
        edgecolor="black",
    )
    plt.title(f"Histograma para NSE: {sel}")
    plt.xlabel("Puntuaciones")
    plt.ylabel("Frecuencia")

plt.tight_layout()
plt.show()

# Create frequency polygon.
plt.figure(figsize=(10, 6))
for sel in ["Bajo", "Medio", "Alto"]:
    subset = df[df["NSE"] == sel]
    sns.histplot(
        subset["PuntuacionesAjustadas"],
        kde=True,
        stat="density",
        element="step",
        fill=False,
        label=f"NSE: {sel}",
    )
    plt.title("Poligonos de frecuencia por NSE")
    plt.xlabel("Puntuaciones")
    plt.ylabel("Densidad")
    plt.legend(title="Nivel Socioeconomico")

plt.show()

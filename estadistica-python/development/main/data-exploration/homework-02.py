import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
from statsmodels.graphics.factorplots import interaction_plot

resistencia = [
    15.29,
    15.89,
    16.02,
    16.56,
    15.46,
    16.91,
    16.99,
    17.27,
    16.85,
    16.35,
    17.23,
    17.81,
    17.74,
    18.02,
    18.37,
    12.07,
    12.42,
    12.73,
    13.02,
    12.05,
    12.92,
    13.01,
    12.21,
    13.49,
    14.01,
    13.30,
    12.82,
    12.49,
    13.55,
    14.53,
]
templado = ["Rapido"] * 15 + ["Lento"] * 15
grosor = ([8] * 5 + [16] * 5 + [24] * 5) * 2

templado = np.random.choice(a=["Rapido", "Lento"], size=30, p=[0.5, 0.5])
grosor = np.random.choice(a=[8,16,24],size=30,p=[0.35,0.35,0.3])
resistencia = np.random.normal(loc=15.3, scale=2.5, size=30)

# Set datos.
datos = {"Templado": templado, "Grosor": grosor, "Resistencia": resistencia}
df = pd.DataFrame(data=datos)

# Set boxplot.
plt.figure(figsize=(10, 6))
sns.set_theme(style="darkgrid")

# Graficar templado vs resistencia.
plt.subplot(1, 2, 1)
sns.boxplot(x="Templado", y="Resistencia", data=df, palette="Spectral")
sns.swarmplot(x="Templado", y="Resistencia", data=df, color="blue", alpha=0.4)
plt.title("Templado vs Resistencia")

# Graficar grosor vs resistencia.
plt.subplot(1, 2, 2)
sns.boxplot(x="Grosor", y="Resistencia", data=df, palette="Spectral")
sns.swarmplot(x="Grosor", y="Resistencia", data=df, color="blue", alpha=0.5)
plt.title("Grosor vs Resistencia")

# Resistencia vs Templado y Grosor.
plt.subplots(1, 1, figsize=(10, 6))
sns.boxplot(x="Templado", y="Resistencia", hue="Grosor", data=df)
plt.title("Resistencia vs Templado y Grosor")

# Calculo de la media y la desviacion estandar de la resistencia por cada tipo de templado.
print("Resistencia media y desviacion tipica por templado")
df.groupby("Templado")["Resistencia"].agg(["mean", "std"])

# Calculo de la media y la desviacion estandar de la resistencia por cada tipo de grosor en cda tipo de templado.
print("Resistencia media y desviacion tipica por el templado y grosor.")
df.groupby(["Templado", "Grosor"])["Resistencia"].agg(["mean", "std"])

# Graficos de interaccion.
fig, ax = plt.subplots(figsize=(6, 4))
fig = interaction_plot(x=df.Templado, trace=df.Grosor, response=df.Resistencia, ax=ax)

fig, ax = plt.subplots(figsize=(6, 4))
fig = interaction_plot(x=df.Grosor, trace=df.Templado, response=df.Resistencia, ax=ax)

plt.show()

# Test ANOVA
pg.anova(
    data=df, dv="Resistencia", between=["Templado", "Grosor"], detailed=True
).round(4)

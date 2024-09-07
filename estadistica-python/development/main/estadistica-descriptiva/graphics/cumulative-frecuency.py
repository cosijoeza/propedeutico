import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Confi
sns.set_theme(style="darkgrid")

# Datos
np.random.seed(42)

sizeData = 1000
# Media 70 y Desviacion 15
score = np.random.normal(loc=70, scale=15, size=sizeData)

schoolKind = np.random.choice(
    ["Publica", "Privada", "Charther"], size=sizeData, p=[0.5, 0.3, 0.2]
)
# Data frame
df = pd.DataFrame({"Puntuaciones": score, "TipoEscuela": schoolKind})

adjusmentSchool = {"Publica": -3, "Privada": 5, "Charther": 0}
df["PuntuacionesAjustadas"] = df.apply(
    lambda x: x["Puntuaciones"] + adjusmentSchool[x["TipoEscuela"]], axis=1
)

plt.figure(figsize=(10, 6))
for kind in ["Publica", "Privada", "Charther"]:
    subset = df[df["TipoEscuela"] == kind]
    print("f{kind}:\n", subset.head())
    sns.ecdfplot(subset["PuntuacionesAjustadas"], label=f"{kind}")


plt.title("Distribuciones acomulativas por tipo de escuela")
plt.xlabel("Puntuaciones ajustadas")
plt.ylabel("Probabilidad acumulada")
plt.legend(title="tipo de escuela")
plt.grid(True)
plt.show()

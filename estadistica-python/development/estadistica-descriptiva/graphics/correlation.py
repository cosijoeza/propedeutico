# Coeficiente de correlación de pearson.
# Se puede calcular de 2 maneras con pearsonr y con linregress.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, linregress

# Seed for reproducibility.
np.random.seed(0)
studentsSize = 100

# Simulation data.
performanceScore = np.random.normal(loc=70, scale=10, size=studentsSize)
steemLevel = np.random.normal(loc=50, scale=10, size=studentsSize)

# Calculate pearson correlation coefficent.
pearsonCoefficent, pValue = pearsonr(performanceScore, steemLevel)

# Regression line.
slope, intercept, rValue, pValueReg, stdErr = linregress(performanceScore, steemLevel)
print("[Pendiente]:", slope)
print("[Intersección]:", intercept)
print("[Coeficiente de Correlacion Pearson]:", rValue)
print("[P para prueba de hipotesis]:", pValueReg)
print("[Error estandar de la pendiente]:", stdErr)

# Create a scatter plot.
plt.figure(figsize=(10, 6))
plt.scatter(
    performanceScore, steemLevel, color="blue", alpha=0.6, edgecolor="k", label="Datos"
)
plt.plot(
    performanceScore,
    intercept + slope * performanceScore,
    color="red",
    label=f"LineadeRegresion (r={pearsonCoefficent:.2f})",
)

print(f"Coeficiente de correlacion de Pearson:{pearsonCoefficent}")
print(f"Valor p asociado a la correlacion:{pValue}")

# Graphics features.
plt.title("Correlacion entre rendimiento academico y autoestima")
plt.xlabel("Puntuaciones de rendimiento academico")
plt.ylabel("Niveles de autoestima")
plt.legend()
plt.grid(True)

# Show graphics.
plt.show()

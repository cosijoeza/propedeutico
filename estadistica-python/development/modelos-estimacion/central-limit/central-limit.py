import numpy as np
import matplotlib.pyplot as plt

# Data simulation, matrix 100*40
mean = 5
samples = np.random.exponential(scale=mean, size=(100, 40))

# Create array with calculate mean by row; Axis = 1 -> Horizontal.
samplesMean = np.mean(samples, axis=1)
theoreticalMean = mean
standarDeviation = mean / np.sqrt(40)

# Generate X data.
x = np.linspace(
    start=theoreticalMean - 3 * standarDeviation,
    stop=theoreticalMean + 3 * standarDeviation,
    num=100,
)

# Calculate normal distribution.
exponent = -1 * (((x - theoreticalMean) ** 2) / (2 * standarDeviation**2))
numerator = np.exp(exponent)
denominator = 1 / (standarDeviation * np.sqrt(2 * np.pi))
y = denominator * numerator

print(f"Media muestral:{np.mean(samplesMean):.10f}")
print(f"Media teorica:{mean:.10f}")

# Create graphics.
plt.figure(figsize=(10, 6))
plt.hist(
    samplesMean,
    bins=30,
    density=True,
    alpha=0.5,
    label="Distibucion de las medias muestrales",
)
plt.plot(x, y, color="red", label="Distribucion normal teorica")
plt.xlabel("Media")
plt.ylabel("Densidad")
plt.title("Teorema central del limite")
plt.legend()
plt.show()

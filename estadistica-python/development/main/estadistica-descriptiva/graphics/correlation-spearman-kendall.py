import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, kendalltau

# Seed for reproducibility.
np.random.seed(0)
studentSize = 100

# Simulation data.
performanceScore = np.random.normal(loc=70, scale=10, size=studentSize)
steemLevel = np.random.normal(loc=50, scale=15, size=studentSize)

# Calculate Spearman coefficent correlation.
spearmanCoefficent, pValueSpearman = spearmanr(performanceScore, steemLevel)

# Calculate Kendal correlation coefficent.
kendallCoefficent, pValueKendall = kendalltau(performanceScore, steemLevel)

print(f"[Coeficiente de correlacion de Spearman]:{spearmanCoefficent}")

print(f"[Valor P asociado a Spearman]:{pValueSpearman}")

print(f"[Coeficiente de correlacion de Kendall]:{kendallCoefficent}")

print(f"[Valor P asociado a Kendall]:{pValueKendall}")

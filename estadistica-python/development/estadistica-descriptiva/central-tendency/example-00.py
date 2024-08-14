import numpy as np
import pandas as pd
from scipy import stats

# Seed.
np.random.seed(42)

# Set information into a map.
data = {
    "Cloridad": np.random.randint(1, 11, 100),
    "Interaccion": np.random.randint(1, 11, 100),
    "Apoyo": np.random.randint(1, 11, 100),
}

# Set information into a data frame.
df = pd.DataFrame(data)

# Get central tendency information.
means = df.mean()
medians = df.median()
modes = df.mode().loc[0]

# Results.
print("Medias:\n", means, "\n")
print("Medians:\n", medians, "\n")
print("Modes:\n", modes, "\n")

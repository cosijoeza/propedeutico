# LIKERT SCALE
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Genere information.
np.random.seed(42)
data = {
    "School-A": np.random.choice(
        [1, 2, 3, 4, 5], size=100, p=[0.05, 0.15, 0.5, 0.20, 0.10]
    ),
    "School-B": np.random.choice(
        [1, 2, 3, 4, 5], size=100, p=[0.1, 0.2, 0.4, 0.2, 0.1]
    ),
    "School-C": np.random.choice(
        [1, 2, 3, 4, 5], size=100, p=[0.15, 0.35, 0.30, 0.15, 0.05]
    ),
}

# Set to dataframe.
df = pd.DataFrame(data)

# Set boxplot.
sns.boxplot(data=df)

# Set labels.
plt.title("School Weather")
plt.xlabel("School")
plt.ylabel("Grade (Likert Scale)")
plt.show()

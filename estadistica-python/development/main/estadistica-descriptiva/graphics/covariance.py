# Calculate covariance matrix.
import numpy as np
import pandas as pd

# Data simulation.
np.random.seed(42)
studentSize = 50

# Generate score random data.
mathScore = np.random.normal(loc=75, scale=10, size=studentSize)
scienceScore = np.random.normal(loc=70, scale=12, size=studentSize)
languageScore = np.random.normal(loc=78, scale=8, size=studentSize)

# Generate time random data.
studyMathTime = np.random.normal(loc=5, scale=1.5, size=studentSize)
studyScienceTime = np.random.normal(loc=4, scale=1.2, size=studentSize)
studyLanguageTime = np.random.normal(loc=4.5, scale=1.3, size=studentSize)

# Create a matrix, array is a row.
data = np.vstack(
    (
        mathScore,
        scienceScore,
        languageScore,
        studyMathTime,
        studyScienceTime,
        studyLanguageTime,
    )
)
# Covariance matrix.
covarianceMatrix = np.cov(data)

# Set to dataframe as row.
x1 = pd.Series(covarianceMatrix[0])
x2 = pd.Series(covarianceMatrix[1])
x3 = pd.Series(covarianceMatrix[2])
x4 = pd.Series(covarianceMatrix[3])
x5 = pd.Series(covarianceMatrix[4])
x6 = pd.Series(covarianceMatrix[5])

df = pd.DataFrame(
    [list(x1), list(x2), list(x3), list(x4), list(x5), list(x6)],
    columns=[
        "PuntMate",
        "PuntCien",
        "PuntLeng",
        "HrsMate",
        "HrsCien",
        "HrsLeng",
    ],
)

print("[Matriz de covarianza]:")
print(df)

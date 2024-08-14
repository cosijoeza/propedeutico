import numpy as np
import pandas as pd
from scipy import stats

# Seed.
np.random.seed(42)

data = {
    'Cloridad': np.random.randint(1,11,100),
    'Interaccion': np.random.randint(1,11,100),
    'Apoyo': np.random.randint(1,11,100)
}
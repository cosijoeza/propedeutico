# Caculate median using numpy.
import numpy as np

data = [5, 10, 15, 20, 25]

data_np = np.array(data)
median_np = np.median(data_np)

print("Median from ", data_np, " is ", median_np)

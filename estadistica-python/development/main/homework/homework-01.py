# Tres trabajadores de una cadena de montaje van a comparar su efectividad. Se recoge el tiempo
# que tarda cada trabajador en realizar su tarea sobre las siguientes 10 unidades que pasan por
# su punto de la cadena.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==================================== (1) ====================================
workerA = np.array([4.44, 4.77, 6.56, 5.07, 5.13, 6.72, 5.46, 3.73, 4.31, 4.55])
workerB = np.array([6.22, 5.36, 5.40, 5.11, 4.44, 6.77, 5.50, 3.03, 5.70, 4.53])
workerC = np.array([3.93, 4.78, 3.97, 4.27, 4.37, 3.31, 5.84, 5.15, 3.86, 6.25])

# Tenemos que decidir si hay algun trabajador más rapido o no. Para ello calculamos las medias del tiempo
data = {"WorkerA": workerA, "WorkerB": workerB, "WorkerC": workerC}
df = pd.DataFrame(data)

print(
    "Mean-WorkerA: {:.4f}\nMean-WorkerB: {:.4f}\nMean-WorkerC: {:.4f}".format(
        df["WorkerA"].mean(), df["WorkerB"].mean(), df["WorkerC"].mean()
    )
)

# Set boxplot.
sns.boxplot(data=df)

# Set labels.
plt.title("HOURS BY WORKERS")
plt.xlabel("Workers")
plt.ylabel("Hours worked")
plt.show()
# Por lo tanto el más rapido ha sido el C.
# Pero se ve que los tiempos de cada trabajador fluctuan, opor lo que tal vez, con
# otra muestra de los mismos trabajadores, el ganador pordia haber sido otro.

# ==================================== (2) ====================================
workerA = np.array([5.01, 5.04, 5.22, 5.07, 5.08, 5.24, 5.11, 4.94, 5.00, 5.02])
workerB = np.array([5.18, 5.09, 5.09, 5.06, 5.00, 5.23, 5.10, 4.86, 5.12, 5.01])
workerC = np.array([4.51, 4.59, 4.51, 4.54, 4.55, 4.45, 4.70, 4.63, 4.50, 4.74])
# Tenemos que decidir si hay algun trabajador más rapido o no. Para ello calculamos las medias del tiempo
data = {"WorkerA": workerA, "WorkerB": workerB, "WorkerC": workerC}
df = pd.DataFrame(data)

print(
    "Mean-WorkerA: {:.4f}\nMean-WorkerB: {:.4f}\nMean-WorkerC: {:.4f}".format(
        df["WorkerA"].mean(), df["WorkerB"].mean(), df["WorkerC"].mean()
    )
)

# Set boxplot.
sns.boxplot(data=df)

# Set labels.
plt.title("HOURS BY WORKERS")
plt.xlabel("Workers")
plt.ylabel("Hours worked")
plt.show()

# ==================================== (3) ====================================
np.random.seed(123)
n = 10
morning = np.random.normal(loc=5, scale=1, size=n)
afternoon = np.random.normal(loc=5, scale=1, size=n)
night = np.random.normal(loc=5, scale=1, size=n)

data = {"Morning": morning, "Afternoon": afternoon, "Night": night}
df = pd.DataFrame(data=data)
print(df)

print(
    "Mean-Morning: {:.4f}\nMean-Afternoon {:.4f}\nMean-Nignt {:.4f}".format(
        df["Morning"].mean(), df["Afternoon"].mean(), df["Night"].mean()
    )
)
# Set boxplot.
sns.set_theme(style="darkgrid")
sns.boxplot(data=df)
# Set labels.
plt.title("title")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

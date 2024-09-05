# Supongamos que deseamos estimar un intervalo de confianza
# del 95% para la media de una muestra de calificaciones.
# Utilizaremos la Distribucion t en Python para realizar esta
# estimacion.
import numpy as np
import scipy.stats as stats

# Datos de las calificaciones de una muestra.
calificaciones = [86, 90, 92, 88, 87, 84, 91, 89, 86, 87]

# Nivel de confianza.
confianza = 0.95

# Grados de libertad.
df = len(calificaciones) - 1

# Media y desviacion estandar de la muestra
media_muestra = np.mean(calificaciones)
# ddof= 1 par acalcular la desviacion estandar muestral.
desviacion_muestra = np.std(calificaciones, ddof=1)

# Valor critico de t.
valorCritico = stats.t.ppf((1 + confianza))

# # Error estandar.
errorEstandar = desviacion_muestra / np.sqrt(len(calificaciones))

# Limites del intervalo de confianza.
intervalo_inferior = media_muestra - valorCritico * errorEstandar
intervalo_superior = media_muestra + valorCritico * errorEstandar

print("Intervalo de confianza al {confianza*100}%: ({intervalo_inferior:2f})")
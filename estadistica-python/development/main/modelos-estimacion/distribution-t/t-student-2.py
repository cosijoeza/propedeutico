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
# Nivel de significancia.
significancia = 1 + confianza
# Grados de libertad.
gradosLibertad = len(calificaciones) - 1

# Media y desviacion estandar de la muestra
mediaMuestra = np.mean(calificaciones)
# ddof= 1 par acalcular la desviacion estandar muestral.
desviacionMuestra = np.std(calificaciones, ddof=1)
# Valor critico de t.
valorCritico = stats.t.ppf(significancia / 2, gradosLibertad)
# Error estandar.
errorEstandar = desviacionMuestra / np.sqrt(len(calificaciones))

print(
    " Media de la muestra:{:.6f}\n Desviacion de la muestra:{:.6f}\n Valor critico: {:.6f}".format(
        mediaMuestra, desviacionMuestra, valorCritico
    )
)

# Limites del intervalo de confianza.
intervalo_inferior = mediaMuestra - valorCritico * errorEstandar
intervalo_superior = mediaMuestra + valorCritico * errorEstandar

print(
    f"Intervalo de confianza al {confianza*100}%: ({intervalo_inferior:2f}, {intervalo_superior:2f})"
)

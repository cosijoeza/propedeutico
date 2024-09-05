# Supongamos que tenemos una muestra de calificaciones de dos grupos de
# estudiantes (Grupo A y Grupo B) y queremos determinar si existe una
# diferencia significativa en sus promedios. Realizaremos una prueba de
# hipotesis utilizando la distribucion t en Python.
import scipy.stats as stats


# Datos de ,las calificaciones de los dos grupos.
grupo_a = [85, 90, 92, 88, 87, 84, 91, 89, 86, 87]
grupo_b = [78, 82, 80, 88, 86, 79, 83, 81, 85, 84]

# Realizamos un prueba t de dos muestras independientes.
(
    t_stat,
    p_valor,
) = stats.ttest_ind(grupo_a, grupo_b)

print("T Stat:{:7f}, P Valor: {:7f}".format(t_stat, p_valor))
# Establecemos un nivel de significado (alfa)
alfa = 0.05

# Comprobamos si rechazamos la hipotesis nula
if p_valor < alfa:
    print("Hay una diferencia significativa entre los grupos")
else:
    print("No hay evidencia de una diferencia significativa entre los grupos")

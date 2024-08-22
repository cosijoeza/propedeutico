datos = dict(
    Nombre="Juan Perez",
    Fecha=dict(dia=1, mes=12, anyo=1997),
    Amigos=("Alex", "Oscar", "Laura"),
)

# 1
print(" ============== 1.-Cambiar la edad de la persona. ==============")
print(datos)
datos["Fecha"]["dia"] = 28
datos["Fecha"]["mes"] = 7
datos["Fecha"]["anyo"] = 1996
print(datos)

# 2
print("\n===================== 2.-Calcular la edad. =====================")
print("Edad: ", 2024 - datos["Fecha"]["anyo"])

# 3
print("\n================== 3.-Agregar un amigo nuevo ===================")
print(type(datos["Amigos"]))

# 4
print("\n======== 4.-Cambiar la clave fecha por fecha_nacimiento ========")
print(datos)
datos.pop("Fecha")
print(datos)
fecha_nacimiento = dict(dia=28, mes=7, anyo=1996)
datos["fecha_nacimiento"] = fecha_nacimiento
print(datos)

# 5
print("\n======== 5.-Tipo de datos de las claves del diccionario ========")
print("valores =", list(datos.values()))
value_0 = list(datos.values())[0]
value_1 = list(datos.values())[1]
value_2 = list(datos.values())[2]

print(value_0, "\t\t\t\t:", type(value_0))
print(value_1, "\t\t:", type(value_1))
print(value_2, "\t:", type(value_2))

# 6
print("\n====================== 6.-Numero bisiesto ======================")
number = datos["fecha_nacimiento"]["anyo"]
x = number % 4 == 0
y = number % 100 == 0
z = number % 400 == 0
res = (x ^ y) | z
print(number, "\t:", res)

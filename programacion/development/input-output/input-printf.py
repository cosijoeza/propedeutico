var = input()
edad = input("Ingrese Edad:")
print("Tu edad es:", edad)

# ============== READ ==============
var = input()
print(type(var))
var = input()
print(type(var))
var = input()
print(type(var))
var = input()
print(type(var))

# ============== TYPE ==============
nombre = input("Escribe tu nombre:")
print(type(nombre), nombre)
edad = input("Escribe tu edad:")
print(type(edad), edad)
peso = input("Escribe tu peso:")
print(type(peso), peso)


# ============== CAST ==============
nombre = input("Nombre:")
print(type(nombre), nombre)

edad = int(input("Edad:"))
print(type(edad), edad)

peso = float(input("Peso:"))
print(type(peso), peso)

# ============== PRINTF ==============
n = 4
print("Hola mundo")
print("El valor de n es:", n)

nombre = "Juan Perez"
edad = 25
estatura = 1.79

print("Nombre:", nombre, "Edad:", edad, "Estatura:", estatura)
print("Nombre:", nombre, "\nEdad:", edad, "\nEstatura:", estatura)
print("Nombre:\"", nombre, "\"\nEdad:\"", edad, "\"\nEstatura:\"", estatura,"\"")

# ============== SEVERAL MESSAGES, DELETE NEXT LINE ==============
print("Hola mundo!!!")
print("Hola mundillo!!!")

print("Otro mensaje", end=" ")
print("De nuevo")

print("Hola", end=" ")
print("Hola")

print("Hola", end=":")
print("Hola")

# ============== STRING FORMATT ==============
base = 3.1415
altura = 11.7341
area = (base * altura) / 2
print("Base {:.2f}, Altura {:.2f}, Area {:.3f}".format(base, altura, area))
print("Calculo: {2:.2f} es ({0:.2f} * {1:.2f})/2".format(base, altura, area))

datos = [
    dict(
        Nombre="Pedro Picapieda",
        Fecha=dict(dia=13, mes=9, anyo=1977),
        Peso=65.349,
        Sueldo=13020.34986898,
    ),
    dict(
        Nombre="Luis Marmol",
        Fecha=dict(dia=11, mes=9, anyo=1975),
        Peso=55.467,
        Sueldo=11000,
    ),
    dict(
        Nombre="Betty Marmol",
        Fecha=dict(dia=25, mes=11, anyo=1980),
        Peso=45,
        Sueldo=0,
    ),
    dict(
        Nombre="Vilma Picapiedra",
        Fecha=dict(dia=4, mes=8, anyo=1981),
        Peso=39,
        Sueldo=0,
    ),
]
campos = ["Nombre", "Edad", "Peso", "Sueldo"]
linea = "-" * 50

print(linea)
print("|{0:20}|{1:6}|{2:9}|{3:10}|".format(campos[0], campos[1], campos[2], campos[3]))
print(linea)
print(
    "|{0:20}|{1:6}|{2:9.2f}|{3:10.3f}|".format(
        datos[0]["Nombre"],
        2024 - datos[0]["Fecha"]["anyo"],
        datos[0]["Peso"],
        datos[0]["Sueldo"],
    )
)
print(linea)
print(
    "|{0:20}|{1:6}|{2:9.2f}|{3:10.3f}|".format(
        datos[1]["Nombre"],
        2024 - datos[1]["Fecha"]["anyo"],
        datos[1]["Peso"],
        datos[1]["Sueldo"],
    )
)
print(linea)
print(
    "|{0:20}|{1:6}|{2:9.2f}|{3:10.3f}|".format(
        datos[2]["Nombre"],
        2024 - datos[2]["Fecha"]["anyo"],
        datos[2]["Peso"],
        datos[2]["Sueldo"],
    )
)
print(linea)
print(
    "|{0:20}|{1:6}|{2:9.2f}|{3:10.3f}|".format(
        datos[3]["Nombre"],
        2024 - datos[3]["Fecha"]["anyo"],
        datos[3]["Peso"],
        datos[3]["Sueldo"],
    )
)
print(linea)

dic_a = {"nombre": "Matuzalem", "edad": 96, "ciudad": "Israel"}
dic_b = {1: "uno", 2: "dos", 3: "tres"}
dic_c = {(2, 3, 5): "un rango", "clave": [1, 2, 3]}

print(dic_a)
print(dic_b)
print(dic_c)

d1 = {"Nombre": "Juan", "Edad": 19, "Matricula": "ic2014020423"}
print(d1)

d2 = dict([("Nombre", "Juan"), ("Edad", 19), ("Matricula", "ic2014020423")])
print(d2)

# From constructor.
print("========== From Constructor ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024003756")
print(d)

# Set data to dictionary.
print("\n========== Set data to dictionary ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024003700")
print(d)
d["Nombre"] = "Erik"
print(d)
d["Direccion"] = "Acatlima 25"
print(d)

# Access to dictionary.
print("\n========== Access to dictionary ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024001")
print("dictionary[Nombre] = ", d["Nombre"])
print("dictionary[Edad]   = ", d["Edad"])
print("dictionary[Matricula] = ", d["Matricula"])

# Access to dictionary with condition.
print("\n========== Access to dictionary with condition. ==========")
print(d)
print("get(Nombre) = ", d.get("Nombre"))
print("get(Nombre,No existe) = ", d.get("Nombre", "No existe"))
print("get(Apellido,No existe) = ", d.get("Apellido", "No existe"))
print("get(Matricula,No existe) = ", d.get("Matricula", "No existe"))
print("get(Enfermedades,No existe) = ", d.get("Enfermedades", "No existe"))

# Nested dictionaries.
print("\n========== Nested dictionaries ==========")
d = dict(
    Nombre="Juan",
    Edad=19,
    Matricula="ic2024001",
    bornDate=dict(
        day=28,
        month=7,
        year=2021,
    ),
)
print(d)
print(type(d["bornDate"]))

fecha = dict(
    day=28,
    month=7,
    year=2021,
)

d2 = dict(Nombre="Juan", Edad=19, Matricula="ic2024001", bornDate=fecha)
print(d2)
print(type(d2["bornDate"]))

# Clean dictionary.
print("\n========== Clean dictionary ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024001")
print(d)
d.clear()
print(d)

# Dictionary to a list.
print("\n========== Dictionary to a list ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024001")
print(d.items())
print(list(d.items()))
print(list(d.items())[1])
print(list(d.items())[1][0])
print(list(d.items())[1][1])

# Keys to a list.
print("\n========== Keys to a list ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024001")
print(d.keys())
print(list(d.keys()))
print(list(d.keys())[1])

# Values to a list.
print("\n========== Values to a list ==========")
d = dict(Nombre="Juan", Edad=19, Matricula="ic2024001")
print(d.values())
print(list(d.values()))
print(list(d.values())[2])

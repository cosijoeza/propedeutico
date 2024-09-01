# print("Tabla de multiplicar")
# n = int(input("Dame un numero entre 0 y 10: "))
# cont = 0
# while cont <= 10:
#     print("{:3d} * {:3d} = {:3d}".format(n, cont, n * cont))
#     cont = cont + 1
# print("Fin")


# print("Tabla de multiplicar")
# n = int(input("Dame un numero entre 0 y 10: "))
# cont = 10
# while cont >= 0:
#     print("{:3d} * {:3d} = {:3d}".format(n, cont, n * cont))
#     cont = cont - 1
# print("Fin")

# print("Indice")
# contUni = 1
# while contUni <= 3:
#     print("{:3d} Unidad".format(contUni))
#     contTema = 1
#     while contTema <= 3:
#         print("{:5d}.{:d} Tema".format(contUni, contTema))
#         contTema = contTema + 1
#     contUni = contUni + 1
# print("Fin")

# print("Indice")
# contUni = 1
# while contUni <= 2:
#     print("{:3d} Unidad".format(contUni))
#     contTema = 1
#     while contTema <= 2:
#         subTema = 1
#         print("{:5d}.{:d} Tema".format(contUni, contTema))
#         while subTema <= 3:
#             print("{:8d}.{:d}.{:d} subTema ".format(contUni, contTema, subTema))
#             subTema += 1
#         contTema = contTema + 1
#     contUni = contUni + 1
# print("Fin")

# print("Es primo?")
# n = int(input("Dame un numero entre 2 y 100: "))
# divisores = 0
# cont = 1
# while cont <= n:
#     if n % cont == 0:
#         divisores = divisores + 1
#     cont += 1
# if divisores == 2:
#     print("Es primo")
# else:
#     print("No es primo")
# print("Fin")

# print("Divisores")
# n = int(input("Dame un numero positivo: "))
# cont = 1
# while cont <= n:
#     if n % cont == 0:
#         print("{:3d}".format(cont))
#     cont += 1
# print("Fin")

# print("Es palindroma?")
# cadena = " atar a la rata"
# cadena = " anita lava la tina  "
# cadena = "oso "
# cadena = cadena.replace(" ", "")
# print(cadena)
# ini = 0
# fin = len(cadena) - 1
# while ini < fin:
#     if cadena[ini] != cadena[fin]:
#         break
#     ini += 1
#     fin += -1
# if ini >= fin:
#     print("{:} es palindroma".format(cadena))
# else:
#     print("{:} no es palindroma".format(cadena))


# print("Vocales")
# voc = dict(a=0, e=0, i=0, o=0, u=0)
# cad = "universidad tecnologica de la mixteca"
# cad = "cosi"
# i = 0
# while i < len(cad):
#     if (
#         cad[i] == "a"
#         or cad[i] == "e"
#         or cad[i] == "i"
#         or cad[i] == "o"
#         or cad[i] == "u"
#     ):
#         voc[cad[i]] = voc[cad[i]] + 1
#     i += 1
# print(voc)

# lista = [2, 4, 3, 34, 22]
# for x in lista:
#     print(x)
# print("Fin")

# tupla = (2, 4, 3, 34, 22)
# for x in tupla:
#     print(x)
# print("Fin")

# cadena = "Hola mundo"
# for x in cadena:
#     print(x)
# print("Fin")

# conjunto = set(["Hola", "Bienvenido", "Ciencia", "Hola", "Datos"])
# for x in conjunto:
#     print(x)
# print("Fins")

# Comienza en 1 y termina nen 20, avanza en 4
# for contador in range(1,20,4):
#     print(contador)
# print("Fin")

# {:10s} imprime 10 caracteres y si faltan pon espacios
# diccionario = dict(Nombre=["Juan", "Perez"], Edad=27, Localidad="Huajuapan")
# for e in diccionario:
#     print("{:10s}:{:}".format(e, diccionario[e]))
# print("Fin")

# diccionario = dict(Nombre=["Juan", "Perez"], Edad=27, Localidad="Huajuapan")
# for c, v in diccionario.items():
#     print("{:10s}:{:}".format(c, v))
# print("Fin")


# meses = [
#     ("Enero", 1),
#     ("Febrero", 2),
#     ("Marzo", 3),
#     ("Abril", 4),
#     ("Mayo", 5),
#     ("Junio", 6),
#     ("Julio", 7),
#     ("Agosto", 8),
#     ("Septiembre", 9),
#     ("Octubre", 10),
#     ("Noviembre", 11),
#     ("Diciembre", 12),
# ]
# for m, n in meses:
#     print("{:12s}:{:5d}".format(m, n))
# print("Fin")

# print("Menu")
# opcion = 1
# while opcion != 0:
#     print("1.- Leer")
#     print("2.- Ver")
#     print("3.- Escribir")
#     print("0.- Salir")
#     opcion = int(input("Selecciona una opcion del menu: "))
#     if opcion == 1:
#         print("            Leyedo ...")
#     elif opcion == 2:
#         print("            Viendo ...")
#     elif opcion == 3:
#         print("            Escribiendo ...")
#     elif opcion == 0:
#         print("         ... Adios ...")
#     else:
#         print("      Opcion invalida ....")

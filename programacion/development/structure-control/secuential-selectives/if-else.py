# Secuential.
print("Calculando el area de un triangulo rectangulo")
base = float(input("Dame el ancho del triagulo rectangulo: "))
altura = float(input("Dame el alto del triangulo rectangulo:"))
area = (base * altura) / 2
print("El area del triangulo rectangulo es {:.2f}".format(area))


import math

# Selective simple.
number = int(input("Dame un numero: "))
if number >= 0:
    print("La raiz cuadrada es {:.3f}".format(math.sqrt(number)))
print("continua")

number = int(input("Dame un numero: "))
if number >= 0 and number <= 9:
    print("El numero {:} es digito".format(number))
print("continua")


# Composite selective.
number = int(input("Dame un numero: "))
if number >= 0 and number <= 9:
    print("El numero {:} es digito".format(number))
else:
    print("El numero {:} no es digito".format(number))
print("continua")

cousins = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]
number = int(input("Dame un numero entre 2 y 100: "))
if (number in cousins) == True:
    print("El numero {:} es primo".format(number))
else:
    print("El numero {:} no es primo".format(number))
print("continua")

# Selectives elif.
digit = int(input("Dame un digito: "))
if digit == 0:
    print("Cero")
elif digit == 1:
    print("Uno")
elif digit == 2:
    print("Dos")
elif digit == 3:
    print("Tres")
elif digit == 4:
    print("Cuatro")
else:
    print("No es digito")

print("Tipos de triangulos")
a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))
if (a == b) and (b == c):
    print("Equilatero")
elif a != b and b != c and a != c:
    print("Escaleno")
else:
    print("Isosceles")

# Nested selective.
print("Tipos de triangulos")
a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))
if a == b and b == c:
    print("Equilatero")
else:
    if a == b or a == c or b == c:
        print("Isoceles")
    else:
        print("Escaleno")

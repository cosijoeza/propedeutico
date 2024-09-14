# ================= FACTORIAL  =================
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Dame un numero: "))
print(factorial(n))


# ================= MULTIPLICACION =================
def multiplicacion(n, m):
    if m == 0:
        return 0
    return n + multiplicacion(n, m - 1)


n = int(input("Dame un numero: "))
m = int(input("Dame un numero: "))
print(multiplicacion(n, m))

# ================= DIVISION =================
def division(n, m):
    if m > n:
        return 0
    return 1 + division(n - m, m)


n = int(input("Dame un numero: "))
m = int(input("Dame un numero: "))
print(division(n, m))


# ================= POTENCIA =================
def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)


n = int(input("Dame un numero: "))
m = int(input("Dame un numero: "))
print(potencia(n, m))


# ================= SUMA ARREGLO =================
def suma(A, i, l):
    print(A[i:])
    if i == l:
        return 0
    return A[i] + suma(A, i + 1, l)


A = [3, 6, 2, 9, 15, 24]
print(suma(A, 0, 6))


# ================= FIBONACCI =================
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Dame un numero: "))
print(fibonacci(n))


# ================= IMPRIMIR CADENA =================
def imprimir(A, i, l):
    if i == l:
        print()
    else:
        print(A[i], end="")
        imprimir(A, i + 1, l)


imprimir("Hola", 0, 4)

# ================= IMPRIMIR CADENA HACIA ATRAS =================


def imprimir(A, i, l):
    if i == l:
        print()
    else:
        imprimir(A, i + 1, l)
        print(A[i], end="")


imprimir("Hola", 0, 4)

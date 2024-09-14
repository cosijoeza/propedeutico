# # [2] Realizar una funcion recursica que dados 2 arreglos de la misma longitud devuelva
# def equalsArray(A, B, i, l):
#     if A[i] != B[i]:
#         return False
#     elif i == l:
#         return True
#     return equalsArray(A, B, i + 1, l)


# A = [4, 54, 3, 67, 8, 50, 3]
# B = [4, 54, 3, 67, 8, 50, 7]
# l = len(A)
# print(equalsArray(A, B, 0, l))


# [3]
def mcd(a, b):
    if a == b:
        print("El maximo comun divisor es:{}".format(a))
    elif a > b:
        mcd(a - b, b)
    else:
        mcd(a, b - a)


a = 18
b = 24
mcd(a, b)
a = 27
b = 100
mcd(a, b)
a = 86
b = 78
mcd(a, b)
# print("El maximo comun divisor de {a} y {b} es { mcd(a, b)}")

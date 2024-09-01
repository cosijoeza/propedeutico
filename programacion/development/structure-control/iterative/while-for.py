import random

# (1)
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print("\n")
# (2)
# words = [
#     "universidad tecnologica de la mixteca",
#     "maestria en ciencia de datos",
#     "el que nada sabe, nada teme",
#     "cosijoeza",
#     "MELCHOR"
# ]
# vocals = dict(a=0, e=0, i=0, o=0, u=0)

# for cad in words:

#     # Count vocals.
#     i = 0
#     while i < len(cad):
#         if (
#             cad[i] == "a"
#             or cad[i] == "e"
#             or cad[i] == "i"
#             or cad[i] == "o"
#             or cad[i] == "u"
#         ):
#             vocals[cad[i]] = vocals[cad[i]] + 1
#         i += 1
#     print(cad)

#     # Show vocals.
#     for c, v in vocals.items():
#         for i in range(v):
#             print(c, end="")
#     print("")

#     # Reboot counters.
#     vocals['a'] = 0
#     vocals['e'] = 0
#     vocals['i'] = 0
#     vocals['o'] = 0
#     vocals['u'] = 0

# (3)
# num = 996
# cont = 1
# print("{:5d}".format(num), end="")
# while cont <= num:
#     if (num % cont) == 0:
#         # Verify if is a prime number.
#         divisorsNumber = 0
#         primeCounter = 1
#         while primeCounter <= cont:
#             if (cont % primeCounter) == 0:
#                 divisorsNumber = divisorsNumber + 1
#             primeCounter += 1
#         if divisorsNumber == 2:
#             print("|{:2d}".format(cont))
#             num = int(num / cont)
#             print("{:5d}".format(num), end="")
#             cont = 0
#     cont += 1
# print("\n")

# (4)
# rows = 5
# cols = 20
# if rows > 0 and cols > 0:
#     for i in range(rows):
#         if i == 0 or i == (rows - 1):
#             for j in range(cols):
#                 print("*", end="")
#         else:
#             for j in range(cols):
#                 if j == 0 or j == (cols - 1):
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#         print("")
# else:
#     print("Informacion invalida")

# (5)
d = dict({})
initial = 0
num = 220
n1 = num
cont = 1
print("{:5d}".format(num), end="")
while cont <= num:
    if (num % cont) == 0:
        # Verify if is a prime number.
        divisorsNumber = 0
        primeCounter = 1
        while primeCounter <= cont:
            if (cont % primeCounter) == 0:
                divisorsNumber = divisorsNumber + 1
            primeCounter += 1
        if divisorsNumber == 2:
            primeNumber = cont
            if primeNumber in d.keys():
                d[primeNumber] += 1
            else:
                d[primeNumber] = 1
            print("|{:2d}".format(primeNumber))
            num = int(num / primeNumber)
            print("{:5d}".format(num), end="")
            cont = 0
    cont += 1
print("\n")

# Show results
i = 0
print("{} = ".format(n1), end="")
for c, v in d.items():
    print("{:d}^{:}".format(c, v), end="")
    if i != (len(d) - 1):
        print("*", end="")
    i += 1
print("")

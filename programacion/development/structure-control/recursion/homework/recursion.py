# [1] Calcular el modulo de 2 numeros.
def mod(numberA, numberB):
    if numberA < numberB:
        return numberA
    return mod(numberA - numberB, numberB)


numberX = 104
numberY = 7
print("El modulo de {} / {} es: {}".format(numberX, numberY, mod(numberX, numberY)))


# [2] Realizar una funcion recursica que dados 2 arreglos de la misma longitud devuelva True sin son iguales
# y Falsa si no lo son.
def equalsArray(arrayA, arrayB, iterator, size):
    if arrayA[iterator] != arrayB[iterator]:
        return False
    elif iterator == size:
        return True
    return equalsArray(arrayA, arrayB, iterator + 1, size)


testArrayA = [4, 54, 3, 67, 8, 50, 3]
testArrayB = [4, 54, 3, 67, 8, 50, 7]
arraySize = len(testArrayA)
print(equalsArray(testArrayA, testArrayB, 0, arraySize - 1))


# [3] Realizar una funcion que dado dos numeros calcule el maximo comun divisor.
def mcd(numberA, numberB):
    if numberA == numberB:
        return numberA
    elif numberA > numberB:
        return mcd(numberA - numberB, numberB)
    else:
        return mcd(numberA, numberB - numberA)


numberX = 18
numberY = 24
print(
    "El maximo comun divisor de {} y {} es {}".format(
        numberX, numberY, mcd(numberX, numberY)
    )
)

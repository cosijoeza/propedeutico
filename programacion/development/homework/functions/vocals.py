# ===================== (1) =====================
# Hacer una funcion que reciba una cadena y que devuelva cuantas vocales hay en esa cadena,
# las letras pueden ser mayusculas o minusculas.
def hasVocals(word):
    vocals = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    number = 0
    for i in range(len(word)):
        if word[i] in vocals:
            number += 1
    return number


cad = "aAcDEedbiuOiu03"
cad = "cosij34"
cad = "univArsidAd tecnologica de la mixtEca"
print("La cadena: '{}' tiene {} vocales".format(cad, hasVocals(cad)))


# ===================== (2) =====================
# Hacer una funcion que reciba que reciba una cadena y que devuelva cuantas consonantes
# hay en esa cadena, las letra
def hasConsonants(word):
    notConsonants = [
        "A",
        "E",
        "I",
        "O",
        "U",
        "a",
        "e",
        "i",
        "o",
        "u",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    ]
    number = 0
    for i in range(len(word)):
        if not (word[i] in notConsonants):
            number += 1
    return number


print("La cadena: '{}' tiene {} consonantes".format(cad, hasConsonants(cad)))


# ===================== (3) =====================
# Hacer una funcion que reciba una lista de núeros y devuelva el mayor.
import random


def mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
c = random.randint(-1000, 1000)
result = mayor(a, b, c)

print("a:{},b:{},c:{}".format(a, b, c))
print("El numero mayor es: {}".format(result))

# ===================== (4) =====================
def toRoman():
    return



# ===================== (5) =====================
def date(year,month,day):
    months = dict(
        {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre",
        }
    )

    if year > 0:
        if month >= 1 and month <= 12:
            if day >= 1 and day <= 31:
                print("{} de {} de {}".format(day, months[month], year))
            else:
                print("Invalid date")
        else:
            print("Invalid date")
    else:
        print("Invalid date")

date(2023,4,6)
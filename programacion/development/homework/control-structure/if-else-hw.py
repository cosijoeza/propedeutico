import math
import random

# (1) Calcular las raices de un polinomio de grado 2.
polynomials = [[1,2,-3],[1, -4, -2], [3, 2, 1], [1, -1, -12], [4, 1, -1], [1, 2, 8], [4, 4, 1]]
index = 6
a = polynomials[index][0]
b = polynomials[index][1]
c = polynomials[index][2]

# Calculate discriminating.
discriminating = (b**2) - (4 * a * c)
print("Para {}, el discriminante es: {}".format(polynomials[index],discriminating))
# Evaluate discriminating.
if discriminating > 0:
    x1 = ((-1 * b) + math.sqrt(discriminating)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(discriminating)) / (2 * a)
    print("Existen dos raices X1 = {0:.4f}, X2 = {1:.4f}".format(x1, x2))
elif discriminating == 0:
    x = (-1 * b) / (2 * a)
    print("Las raices son iguales X1 = X2 = {:.4f}".format(x))
else:
    print("Este polinomio no tiene raices")
print("\n")

#(2) Calcular el mayor de 3 numeros.
a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
c = random.randint(-1000, 1000)
print("a:{},b:{},c:{}".format(a, b, c))

    # Compare numbers.
if a > b and a > c:
    print("El numero mayor es: ",a)
elif b > c:
    print("El numero mayor es: ",b)
else:
    print("El numero mayor es: ",c)

# (3) Dada la fecha de nacimiento de una persona, calcular su edad.
day = 29
month = 7
year = 1992
currentDay = 28
currentMonth = 8
currentYear = 2024
print("\nAnio:{} Mes:{} Dia:{}".format(year, month, day))
if year <= 2024:
    if month >= 1 and month <= 12:
        if day >= 1 and day <= 31:
            # Calculate days.
            days = (currentDay + (31 - day)) % 31
            # Calculate months.
            if day > currentDay:
                months = (currentMonth + (12 - month - 1)) % 12
            else:
                months = (currentMonth + (12 - month)) % 12
            # Calculate years.
            if month < currentMonth:
                years = currentYear - year
            elif month == currentMonth:
                if currentDay >= day:
                    years = currentYear - year
                else:
                    years = currentYear - year - 1
            else:
                years = currentYear - year - 1
            print("Tienes {} anios,{} meses,{} dias".format(years, months, days))
else:
    print("Invalid date")

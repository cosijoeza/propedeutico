import math
import random

# (1)
polynomials = [[1, -4, 2], [3, 2, 1], [1, -1, -12], [4, 1, -1], [1, 2, 8], [4, 4, 1]]
index = 4
a = polynomials[index][0]
b = polynomials[index][1]
c = polynomials[index][2]

# Calculate discriminating.
discriminating = (b**2) - (4 * a * c)
print(discriminating)

# Evaluate discriminating.
if discriminating > 0:
    x1 = ((-1 * b) + math.sqrt(discriminating)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(discriminating)) / (2 * a)
    print("Existen dos raices X1 = {0:.4f}, X2 = {1:.4f}".format(x1, x2))
elif discriminating == 0:
    x = -1 * b
    print("Las raices son iguales X1 = X2 = {:.4f}".format(x))
else:
    print("Este polinomio no tiene raices")

# (2)
a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
c = random.randint(-1000, 1000)
print("a:{},b:{},c:{}".format(a, b, c))
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

# (3)
day = 28
month = 8
year = 2000
currentDay = 28
currentMonth = 8
currentYear = 2024

if year <= 2024:
    if month >= 1 and month <= 12:
        if day >= 1 and day <= 31:
            days = (31 + (currentDay - day)) % 31
            months = (12 + (currentMonth - month)) % 12
            if (month <= currentMonth) and (day <= currentDay):
                years = currentYear - year
            else:
                years = currentYear - year - 1
            print("Tienes {} anios,{} meses,{} dias".format(years, months, days))
else:
    print("Invalid date")

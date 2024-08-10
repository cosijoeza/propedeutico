# Maestría en ciencia de datos - Programacion.
# Cosijoeza Melchor Nolasco.

# Int.
print("\t******INTEGER NUMBERS******")
print("-Int-")
number_a = 2353645324
number_b = 345543543
print(number_a," + ",number_b," = ",number_a+number_b)
print(number_a," / ",number_b," = ",number_a/number_b,"\n")

# Binary.
print("-Binary-")
number_a = 0b10101010010010
number_b = 0b1011110111
print(number_a," - ",number_b," = ",number_a-number_b)
print(number_a," / ",number_b," = ",number_a/number_b,"\n")

# Octal.
print("-Octal-")
number_a = 0o740643651071
number_b = 0o1740562060253236264
print(number_a," * ",number_b," = ",number_a*number_b)
print(number_a," / ",number_b," = ",number_a/number_b,"\n")

# Hexadecimal.
print("-Hexadecimal-")
number_a = 0x2D930E30
number_b = 0x6F17D29F8F3
print(number_a," + ",number_b," = ",number_a+number_b)
print(number_a," / ",number_b," = ",number_a/number_b,"\n")

# Float.
print("\t******DECIMAL NUMBERS******")
print("-Float-")
number_a = 54564.2435432
number_b = -87657.4543563423
number_sum = number_a + number_b
number_sub = number_a - number_b
number_mul = number_a * number_b
number_div = number_a / number_b
print(number_a," + ",number_b," = ",number_sum)
print(number_a," - ",number_b," = ",round(number_sub,3))
print(number_a," * ",number_b," = ","{:.7f}".format(number_mul))
print(number_a," / ",number_b," = ",number_div)
print(number_a," / ",number_b," = ",int(number_div),"\n")

# Complex.
print("\t******COMPLEX NUMBERS******")
print("-Complex-")
number_a = 76423 + 453j
number_b = -9832 + 23j
print(number_a," + ",number_b," = ",number_a+number_b)
print(number_a," - ",number_b," = ",number_a-number_b)
print(number_a," / ",number_b," = ",number_a/number_b,"\n")

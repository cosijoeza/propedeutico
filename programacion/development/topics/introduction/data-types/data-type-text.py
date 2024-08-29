# quotation marks.
print("\n========= Quotation marks =========")
text = "hola \" mundo '"
print(text)

# concatenation.
print("\n========= Concatenation =========")
s1 = "hola"
espacio = " "
s2 = "mundo"
s3 = 5
s4 = "veces"
res = s1 + espacio + s2 + str(s3) + espacio + s4
print(res)

n1 = 7
n2 = 3
n3 = n1 / n2
res = "Los numeros %d entre %d = %f" % (n1, n2, n3)
print(res)

# format strings.
print("\n========= Format Strings =========")
n1 = 23
n2 = 1.31416
res = "Los numeros son: {} y {}".format(n1, n2)
print(res)

n = "Los numeros son{b}{c} y {a}".format(a=5, b=10, c=3.426)
print(res)

a = 15.4
b = 10.98723
x = 3.4
y = 43
s1 = f"a={a} y b={b}"
print(s1)
s2 = f"{x} + {y} = {x+y}"
print(s2)


# Multiply strings.
print("\n========= Multiply Strings =========")
s1 = "Hola " * 3
print(s1)

s2 = "Hola " * 15 + "mundo " * 10
print(s2)

# 'len' function.
print("\n========= 'len' function =========")
s = "Hola mundillo!"
l = len(s)
print(l)

# 'in' function.
print("\n========= 'in' function =========")
s = "mundo" in "hola edmundo!!"
print(s)

c = "mundo" in "Hola crayola!!"
print(c)

# 'split' function.
print("\n========= 'split' function =========")
s1 = "hola.mundo.cruel"
res = s1.split(".")
print(res)
s1 = "hola.mundo.cruel"
res = s1.split(".", 1)
print(res)
s1 = "hola..mundo.cruel"
res = s1.split(".")
print(res)
s1 = "hola..mundo.cruel"
res = s1.split("..")
print(res)
s1 = "hola mundo cruel"
res = s1.split()
print(res)

# 'index' functions.
print("\n========= 'index' function =========")
s = "Hola mundo como estan?"
print(s[0])
print(s[-1])
print(s[2:6])
print(s[1:])

# 'capitalize' function.
print("\n========= 'capitalize' function =========")
s = "Hola mundo"
s = s.capitalize()
print(s)

# 'lower' function.
print("\n========= 'lower' function =========")
s = "Hola mundo"
s = s.lower()
print(s)

# 'upper' function.
print("\n========= 'upper' function =========")
s = "Hola mundo"
s = s.upper()
print(s)

# 'swapcase' function.
print("\n========= 'swapcase' function =========")
s = "Cosijoeza Melchor NOLASCO"
s = s.swapcase()
print(s)

# 'count' function.
print("\n========= 'count' function =========")
s = "Cosijoeza Melchor Cosijoeza Nolasco"
s = s.count("za")
print(s)
s = "Cosijoeza Melchor Cosijoeza Nolasco"
s = s.count(" ")
print(s)
s = "Cosijoeza Melchor Cosijoeza Nolasco"
s = s.count("za", 5)
print(s)
s = "Cosijoeza Melchor Cosijoeza Nolasco"
s = s.count("za", 5, 16)
print(s)

# 'isalnum' function.
print("\n========= 'isalnum' function =========")
s = "1543"
res = s.isalnum()
print(res)  # True.
s = "1543.34"
res = s.isalnum()
print(res)  # False.
s = "hola"
res = s.isalnum()
print(res)  # True.
s = "hola123"
res = s.isalnum()
print(res)  # True.

# 'isalpha' function.
print("\n========= 'isalpha' function =========")
s = "1543"
res = s.isalpha()
print(res)  # False.
s = "1543.34"
res = s.isalpha()
print(res)  # False.
s = "hola"
res = s.isalpha()
print(res)  # True.
s = "hola123"
res = s.isalpha()
print(res)  # False.

# 'isdigit' function
print("\n========= 'isdigit' function =========")
s = "1543"
res = s.isdigit()
print(res)  # True.
s = "1543.34"
res = s.isdigit()
print(res)  # False.
s = "hola"
res = s.isdigit()
print(res)  # False.
s = "hola123"
res = s.isdigit()
print(res)  # False.

# 'strip' function. Clean strings. Delete character.
print("\n========= 'strip' function =========")
s1 = "eeCosijoeza Melchoree"
print(s1.strip("e"))
s1 = "eieCosijoeza Melchoreie"
print(s1.strip("ei"))
s1 = "aieeCosijoeza Melchoreie"
print(s1.strip("ei"))
s1 = " Cosijoeza Melchor "
print(s1.strip())

# 'zfill' function.
print("\n========= 'zfill' function =========")
n = "13456"
res = n.zfill(10)
print(res)
n = "13456"
res = n.zfill(2)
print(res)
n = "hola"
res = n.zfill(8)
print(res)

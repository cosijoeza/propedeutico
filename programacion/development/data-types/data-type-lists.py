# Boolean Numbers.
print("========= Compare numbers =========")
n1 = 9
n2 = 11
n3 = 9
res1 = n1 == n2
res2 = n1 == n3
print(res1)
print(res2)

# Lists.
# 'len' function.
print("\n========= 'len' function =========")
l1 = [5, 2, 8, 4]
l2 = ["cas", "mano", "uva"]
l3 = ["z", 91, "hola", 4.56]
l4 = ["ala", [5, 6, 7]]

print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))

# 'append' function.
print("\n========= 'append' function =========")
l = ["cas", "mano", "uva"]
print(l)
l.append(56)
print(l, "\n")

# 'extend' function.
n = [1, 2, 3, 4, 5, 6]
print(n)
n.extend([7, 8, 9, 10])
print(n, "\n")

n1 = [1, 2, 3, 4]
n2 = [5, 6, 7]
print(n1)
n1.extend(n2)
print(n1, "\n")

# 'insert' method.
print("\n========= 'insert' function =========")
n = [11, 7, 9, 13, 17]
print(n)
n.insert(0, 10)
print(n, "\n")
n = [11, 7, 9, 13, 17]
print(n)
n.insert(2, 10)
print(n, "\n")
n = [11, 7, 9, 13, 17]
print(n)
n.insert(len(n), 10)
print(n, "\n")
n = [11, 7, 9, 13, 17]
print(n)
n.insert(11, 10)
print(n, "\n")

# 'remove' method. Delete same input.
print("\n========= 'remove' function =========")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.remove(4)
print(n)

# 'clear' method.
print("\n========= 'clear' function =========")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.clear()
print(n)

# 'index' method.
print("\n========= 'index' function =========")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
res = n.index(9)
print("n[9] = ", res)
res = n.index(6, 2, 8) # Interval[2,8]
print(res)
res = n.index(8, 2, 8) # Interval[2,8]
print(res)
# res = n.index(8, 2, 5)
# print(res)

# 'count' method.
print("\n========= 'count' function =========")
n = [1, 2, 3, 4, 5, 1, 5, 7, 9, 5]
print(n)
res = n.count(5)
print("'5' is", res, "times")
res = n.count(6)
print("'6' is", res, "times\n")

# 'sort' method.
print("\n========= 'sort' function =========")
n = [1, 2, 3, 4, 5, 1, 5, 7, 9, 5]
print(n)
n.sort()
print(n, "\n")

# n = [1,"hola",-3,[3,2,1]]
# n.sort()      FAILS!!!
# print(n)

# 'sorted' method.
print("\n========= 'sorted' function =========")
n = [1, 2, 3, 4, 5, 1, 5, 7, 9, 5]
print(n)
res = sorted(n)
print(res)
res = sorted(n, reverse=True)
print(res)

# 'reverse' method.
print("\n========= 'reverse' function =========")
n = [1, 2, 3, 4, 5, 1, 5, 7, 9, 5]
print(n)
n.reverse()
print(n)

# 'copy' method.
print("\n========= 'copy' function =========")
n1 = [1, 2, 3, 4, 5, 1, 5, 7, 9, 5]
n2 = n1
n3 = n1.copy()
print("n1 = ", n1)
print("n2 = ", n2)
n1.remove(3)
print("n1 = ", n1)
print("n2 = ", n2)
print("n3 = ", n3)

# index access.
print("\n========= index access =========")
n = [11, 23, 13, 4, 55, 1, 33]
print(n)
res = n[0]
print("n[0]     = ", res)
res = n[2:4]
print("n[2:4]   = ", res)
res = n[2:40]
print("n[2:40]  = ", res)
res = n[-1]
print("n[-1]    = ", res)
res = n[-3]
print("n[-3]    = ", res)

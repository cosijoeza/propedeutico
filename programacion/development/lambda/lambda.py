def retornarNota(student):
    return student[1]


students = [("Cosi", 9.7), ("Pepe", 2.5), ("Deborah", 9.5), ("C arlos", 4.5)]

# students_ordenada = sorted(students, key=retornarNota, reverse=True)
# students_ordenada = sorted(students, key=lambda x: x[0], reverse=True)
# print(students_ordenada)

lista = [1, 2, 3]
retorno = lambda x: x[1] + x[0]
print(retorno(lista))

suma = lambda x, y: x + y
print(suma(5, 6))

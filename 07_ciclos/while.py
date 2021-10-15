i = 0
suma = 0
# a = a + n -> acumulador

while i < 101:
    # suma = suma + i
    suma += i
    i = i + 1

print(suma)

#################################################################################

alumnos = [10, 8.8, 5.6, 4.2, 9.5]
i = 0
size = len(alumnos)

# 0,..., size-1
# [0, size) pertenece a los enteros
while i < size:
    alumno = alumnos[i]
    if alumno >= 9:
        print("Chico de excelencia")
    elif alumno > 5 and alumno < 9:
        print("Puedes hacerlo mejor")
    else:
        print("Ja... que wey")
    i += 1
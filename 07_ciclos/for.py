alumnos = [10, 8.8, 5.6, 4.2, 9.5]

for alumno in alumnos:
    if alumno >= 9:
        print("Chico de excelencia")
    elif alumno > 5 and alumno < 9:
        print("Puedes hacerlo mejor")
    else:
        print("Ja... que wey")

####################################################

suma = 0

# range(a) -> [0,..., a-1]
# range(a,b) -> [a,...., b-1]

for i in range(101):
    suma += i

print(suma)
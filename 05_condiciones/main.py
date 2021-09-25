pelotas = int(input("Ingrese un numero de pelotas: "))

if pelotas == 0:
    print("No hay pelotas")
elif pelotas>0 and pelotas <=2:
    print("Hay pelotas suficientes")
else:
    print("Hay demasiadas pelotas")

#########################################################################

promedio = float(input("Ingresa tu promedio: "))
'''
    0 - 3.9999999 = eres un burro       [0,4)
    4 - 7 = casi mueres       [4,7)
    7 - 9 = puedes mejorar      [7,9)
      > 9 = que matado eres     [9,inf)
'''
if promedio >= 0 and promedio < 4:
    print("Eres un burro")
elif promedio >= 4 and promedio < 7:
    print("Casi mueres")
elif promedio >= 7 and promedio < 9:
    print("Puedes mejorar")
else:
    print("Que matado eres")
import controller

# Programa principal

print("Programa principal")


# print('{} {} {}'.format(True, 34, 'hola'))

print(controller.numNotif())
print(controller.readNotif(5))
controller.deleteNotif(3)
print(controller.numNotif())
print(controller.readNotif(5))

# print(f"Antes: {controller.numNotif()}")
# controller.creatNotif()
# print(f"Despues: {controller.numNotif()}")
# print(controller.readLast())

controller.editNotif(5)
print(controller.readNotif(5))
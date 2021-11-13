import controller

# Programa principal

# print('{} {} {}'.format(True, 34, 'hola'))

# print(controller.numNotif())
# print(controller.readNotif(5))
# controller.deleteNotif(3)
# print(controller.numNotif())
# print(controller.readNotif(5))

# # print(f'Antes: {controller.numNotif()}')
# # controller.creatNotif()
# # print(f'Despues: {controller.numNotif()}')
# # print(controller.readLast())

# controller.editNotif(5)
# print(controller.readNotif(5))

def interaccion():
    print('Que es lo que quieres hacer?')
    print('\t1. Crear una notificacion')
    print('\t2. Editar una notificacion')
    print('\t3. Leer notificacion(es)')
    print('\t4. Eliminar una notificacion')
    print('\t5. Salir')
    opcion = int(input('Opcion: '))
    return opcion

def menuLeer():
    print("Que quieres leer?")
    print('\t1. Leer todos los datos')
    print('\t2. Leer un dato en especifico')
    print('\t3. Leer el ultimo dato')
    opcion = int(input('Opcion: '))
    if opcion == 1:
        print(controller.readAll())
    elif opcion == 2:
        index = int(input('Qué indice quiere leer (numero)? '))
        if controller.numNotif() < index:
            print(controller.readLast())
        else:
            print(controller.readNotif(index))
    elif opcion == 3:
        print(controller.readLast())

def menuEliminar():
    print("Que quieres eliminar?")
    print('\t1. Eliminar el primer dato')
    print('\t2. Eliminar un dato en especifico')
    print('\t3. Eliminar el ultimo dato')
    opcion = int(input('Opcion: '))
    if opcion == 1:
        controller.deleteFirst()
    elif opcion == 2:
        index = int(input('Qué indice quiere eliminar (numero)? '))
        if controller.numNotif() < index:
            controller.deleteLast()
        else:
            controller.deleteNotif(index)
    elif opcion == 3:
        controller.deleteLast()

def tareas(opcion):
    if opcion == 1:
        controller.creatNotif()
    elif opcion == 2:
        index = int(input('Qué indice quiere editar (numero)? '))
        if controller.numNotif() < index:
            controller.editNotif(-1)
        else:
            controller.editNotif(index)
    elif opcion == 3:
        menuLeer()
    elif opcion == 4:
        menuEliminar()
    elif opcion == 5:
        print('Adios')
    else:
        print('Opcion no valida. Ingrese otra opcion\n')

if __name__ == '__main__':
    print('Programa principal')
    resultado = 0
    while resultado != 5:
        resultado = interaccion()
        tareas(resultado)
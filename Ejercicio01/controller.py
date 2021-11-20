# import dataJSON
# from dataJSON import suma

# def hola(nombre):
#     print(dataJSON.hola() + " " + nombre)
#     print(suma(10, 5))

# CRUD -> Create, Read, Update, Delete


from dataJSON import data
# from dataJSON import suma as adicion
import random as rand

def deleteNotif(index):
    data.pop(index-1)

def deleteLast():
    data.pop()

def deleteFirst():
    # data.pop(0)
    deleteNotif(1)

# Tamanio de los datos
def numNotif():
    return len(data)

def readNotif(index):
    return data[index-1]

def readAll():
    return data

def readLast():
    return data[-1]

def creatNotif():
    title = input('Ingrese el titulo: ')
    body =  input('Ingrese el cuerpo de la notificacion: ')
    userId = rand.randint(1, 10)
    idNotif = rand.randint(1, 1000)
    notification = {
        "userId": userId,
        "id": idNotif,
        "title": title,
        "body": body 
    }
    data.append(notification)

def editNotif(index):
    notif = readNotif(index)
    title = input(f"Ingrese el titulo [{notif['title']}]: ")
    body =  input('Ingrese el cuerpo de la notificacion [{}]: '.format(notif['body']))
    if title != '':
        notif['title'] = title
    if body != '':
        notif['body'] = body
    data[index] = notif
    

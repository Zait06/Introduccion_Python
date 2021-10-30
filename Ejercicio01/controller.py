# import dataJSON
# from dataJSON import suma

# def hola(nombre):
#     print(dataJSON.hola() + " " + nombre)
#     print(suma(10, 5))

# CRUD -> Create, Read, Update, Delete


from dataJSON import data

def deleteNotif(index):
    data.pop(index-1)

def deleteLast():
    data.pop()

def numNotif():
    return len(data)

def readNotif(index):
    return data[index-1]

def readAll():
    return data
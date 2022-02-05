usuarios = []

def crearUsuario():
    nombre = input('Ingrese un nombre: ')
    edad = int(input('Ingrese la edad: '))
    usuario = {
        'nombre': nombre,
        'edad': edad
    }
    print(f'Se agrego a {nombre}')
    usuarios.append(usuario)

def agregarUsuario(nombre, edad):
    usuarios.append({'nombre': nombre, 'edad': edad})

def verUsuarios():
    for idx, usuario in enumerate(usuarios):
        print(f'{idx+1}. {usuario["nombre"]} con edad {usuario["edad"]}')

def sumaLista(*args):
    print(sum(args))

def conDic(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    # agregarUsuario('Juan', 20)
    # agregarUsuario('Gina', 25)
    # agregarUsuario('Zait', 23)
    # verUsuarios()
    # crearUsuario()
    # verUsuarios()
    sumaLista(15, 10, 54, 55, 45, 54)
    conDic(nombre='Zait', edad=25, alergias=[])

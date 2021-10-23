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

if __name__ == "__main__":
    agregarUsuario('Juan', 20)
    agregarUsuario('Gina', 25)
    agregarUsuario('Zait', 23)
    verUsuarios()
    crearUsuario()
    verUsuarios()
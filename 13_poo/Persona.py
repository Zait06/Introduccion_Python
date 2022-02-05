'''
Atributos / métodos públicos -> Todo mundo puede acceder a ellos
Atributos / métodos privados -> Solamente pueden ser accedidos internamente por la clase
*Atributos protegidos
'''

class Persona(object):
    msg = "Hola"
    __apodo = "No tengo apodo"

    # Constructor
    def __init__(self, apPat, apMat, nombre):
        self.apPat = apPat
        self.apMat = apMat
        self.nombre = nombre

    # Método toString()
    def __str__(self) -> str:
        return f"{self.nombre} {self.apPat} {self.apMat}"

    def editarApodo(self, apodo):
        self.__apodo = apodo

    def verApodo(self) -> str:
        return self.__apodo

    def saludar(self):
        print(f"{self.msg}, yo soy {self.__apodo}")


if __name__ == "__main__":
    p = Persona("Garcia","Lopez","Javier")

    p.msg = "Que tal"
    print(p.msg)
    print(p.nombre)
    print(p)

    # p.__apodo = "Javercito"

    p.editarApodo("Javiercito")

    # p.saludar()
    print(p.verApodo())
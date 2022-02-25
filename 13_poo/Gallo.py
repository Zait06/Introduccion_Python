from Ave import Ave

class Gallo(Ave):

    def __init__(self):
        super().__init__()
        self.plumaje = "blanco"
        self.cresta = "rojo"
        self._protected = 20
        print(self._protected)

    def volar(self):
        print("No se volar")

    def cantar(self):
        print("Kikiriki")

    def correr(self):
        print("Estoy corriendo")
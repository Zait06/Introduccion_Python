from Ave import Ave

class Colibri(Ave):

    def __init__(self):
        super().__init__()
        self.pico = 5
        self.plumaje = "verde"

    def volar(self):
        print("Estoy volando y tambien lo puedo hacer hacia atras")

    def cantar(self):
        print("Yo no puedo cantar")
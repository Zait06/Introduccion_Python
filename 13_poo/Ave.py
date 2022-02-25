# Esta sera mi clase padre

class Ave(object):

    def __init__(self):
        self.patas = 2
        self.pico = 2  # cm
        self.plumaje = "gris"
        self._protected = 5
    
    def volar(self):
        print("Estoy volando")

    def cantar(self):
        print("pio pio")
from Ave import Ave
from Canario import Canario
from Gallo import Gallo
from Colibri import Colibri

if __name__ == "__main__":
    ave = Ave()
    gallo = Gallo()
    canario = Canario()
    colibri = Colibri()
    
    ave.cantar()
    canario.cantar()
    gallo.cantar()
    colibri.cantar()

    print("")

    print(ave.plumaje)
    print(canario.plumaje)
    print(gallo.plumaje)
    print(colibri.plumaje)

    print("")
    
    gallo.volar()
    ave.volar()
    canario.volar()
    colibri.volar()

    gallo.correr()

    print("")

    print(ave.pico)
    print(canario.pico)
    print(gallo.pico)
    print(colibri.pico)

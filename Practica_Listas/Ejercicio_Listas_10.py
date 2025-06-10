from Lista import List

class Cancion:
    
     def __init__(self, Nom, Artista, Duracion,Reproducciones):
         self.Nom = Nom
         self.Artista = Artista
         self.Duracion = Duracion
         self.Reproducciones = Reproducciones
    
     def __str__(self):
         return f"{self.Nom} -{self.Artista},  {self.Duracion}- {self.Reproducciones}"

Datos_Cancion = [
    Cancion(Nom = "Juan ",Artista = "Arctic Monkeys", Duracion = 1.45, Reproducciones = "Algoritmo" ),
    Cancion(Nom = "Agus",Artista = "Ag", Duracion = 3.00 ,Reproducciones = "Fisica"),
    Cancion(Nom = "Le",Artista = "Cl", Duracion = 2.54,Reproducciones = "Mat"),
    Cancion(Nom = "Clowd",Artista = "Arctic Monkeys", Duracion = 3.46,Reproducciones = "Algoritmo"),
    ]

Lista_1 = List(Datos_Cancion)

def Cancion_mas_larga():
    mayor = 0
    for i in range(len(Lista_1)):
        if mayor < Lista_1[i].Duracion:
            mayor = Lista_1[i].Duracion
    print("La cancion mas larga es: ",mayor)

def Arctic_Monkeys():
    for i in range(len(Lista_1)):
        if  Lista_1[i].Artista == ("Arctic Monkeys"):
                print("Canciones de Arctic Monkeys : ",Lista_1[i].Nom)

def Una_Palabra():
    Espacio = (" ")
    for i in range(len(Lista_1)):
        if " " not in Lista_1[i].Artista:
                print("Artistas de una sola palabra : ",Lista_1[i].Nom)


def Una_Palabra(): # VER QUE TIENE DE DISTINTO CON EL DE ARRIBA
    print("Artistas de una sola palabra:")
    for cancion in Lista_1:
        if " " not in cancion.Artista:
            print(cancion.Artista)



Cancion_mas_larga()
Arctic_Monkeys()
Una_Palabra()
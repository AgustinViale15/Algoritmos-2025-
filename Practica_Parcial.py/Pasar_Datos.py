from Lista import List
from Cola import Cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

class Cancion:
    
     def __init__(self, Nom, Artista):
         self.Nom = Nom
         self.Artista = Artista
    
     def __str__(self):
         return f"{self.Nom} -{self.Artista}"

Datos_Cancion = [
    Cancion(Nom = "Juan ",Artista = "Arctic Monkeys" ),
    Cancion(Nom = "Agus",Artista = "Ag"),
    Cancion(Nom = "Le",Artista = "Cl",),
    Cancion(Nom = "Clowd",Artista = "Arctic Monkeys"),
    ]

Lista_1 = List(Datos_Cancion)
Cola_1 = Cola()

for i in range(len(Lista_1)):
    #Lista_1[i].arribo(Cola,Datos_Cancion)
    Datos = Lista_1[i]
    arribo(Cola_1,Datos)


barrido(Cola_1)

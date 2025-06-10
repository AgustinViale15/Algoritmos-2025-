from Lista import List
class Personajes:
    
     def __init__(self, Nom):
         self.Nom = Nom

    
     def __str__(self):
         return f"{self.Nom}"

Datos_Personajes = [
    Personajes(Nom = "Kang "),
    Personajes(Nom = "Hulk "),
    Personajes(Nom = "Black Widow "),
    Personajes(Nom = "Black Cat "),
    Personajes(Nom = "Iron Man "),
    Personajes(Nom = "Magneto "),
    Personajes(Nom = "Storm "),
    Personajes(Nom = "Venom "),
    Personajes(Nom = "Scarlet Witch "),
    Personajes(Nom = "Abomination "),
    Personajes(Nom = "Adam Warlock "),
    Personajes(Nom = "Angel "),
    Personajes(Nom = "Annihilus "),
    Personajes(Nom = "Ant Man "),
    Personajes(Nom = "Capitan America"),
    ]

Lista_1 =List(Datos_Personajes)


def Cap_America_Recursiva(indice=0):  
    if indice >= len(Lista_1):
        print("Capitan America no esta en la lista")
        return False
    if Lista_1[indice].Nom.strip() == "Capitan America":
        print("Capitan America esta en la lista")
        return True
    return Cap_America_Recursiva(indice + 1)

def Listar_superheroes(indice=0):
    if indice >= len(Lista_1):  
        return
    print(Lista_1[indice].Nom.strip())  
    Listar_superheroes(indice + 1)      


Cap_America_Recursiva()
Listar_superheroes()
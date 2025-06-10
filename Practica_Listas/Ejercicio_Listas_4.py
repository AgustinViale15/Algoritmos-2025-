from Lista import List

class Person:
    
     def __init__(self, nom, ape, dni):
         self.nom = nom
         self.ape = ape
         self.dni = dni
    
     def __str__(self):
         return f"{self.ape}, {self.nom} - {self.dni}"

Personas = [
    Person(nom = "Juan",ape = "Cas", dni = 45),
    Person(nom = "Agus",ape = "Ag", dni = 15),
    Person(nom = "Cle",ape = "Cl", dni = 34),
    Person(nom = "Clowd",ape = "Clo", dni = 65),
    ]
cont = 0

for persona in Personas:
    cont +=1

print("Cantidad de elementos en la lista:",cont)
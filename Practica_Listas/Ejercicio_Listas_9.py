from Lista import List

class Person:
    
     def __init__(self, Nom, Ape, Legajo,Materia,Nota):
         self.Nom = Nom
         self.Ape = Ape
         self.Legajo = Legajo
         self.Materia = Materia
         self.Nota = Nota
    
     def __str__(self):
         return f"{self.Ape}, {self.Nom} - {self.Legajo}- {self.Materia}- {self.Nota}"

Datos_Personas = [
    Person(Nom = "Juan",Ape = "Cas", Legajo = 45, Materia = "Algoritmo",Nota = 7 ),
    Person(Nom = "Agus",Ape = "Ag", Legajo = 15 ,Materia = "Fisica",Nota = 8),
    Person(Nom = "Le",Ape = "Cl", Legajo = 34,Materia = "Mat",Nota = 5),
    Person(Nom = "Clowd",Ape = "Clo", Legajo = 65,Materia = "Algoritmo",Nota = 9),
    ]

Lista_1 = List(Datos_Personas)

Lista_1.add_criterion("Nom", lambda x: x.Nom)
Lista_1.sort_by_criterion("Nom")

def No_desaprobar():
    print("Alumnos que no desaprobaron: ")
    for i in range(len(Lista_1)):
        if Lista_1[i].Nota > 7 :
            print(Lista_1[i].Nom)
def Nombre():
    Letras = ("L")
    for i in range(len(Lista_1)):
        if Lista_1[i].Nom[0] in Letras:
            print("Nombres que comienzan con L",Lista_1[i].Nom)

def Algoritmo():
    
    for i in range(len(Lista_1)):
        if Lista_1[i].Materia == ("Algoritmo"):
            print("Alumnos que cursaron Algoritmo: ",Lista_1[i].Nom)
No_desaprobar()
Nombre()
Algoritmo()
Lista_1.show()
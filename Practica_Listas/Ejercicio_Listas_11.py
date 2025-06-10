from Lista import List

class Personajes:
    
     def __init__(self, Nom, Altura, Edad,Genero,Especie,Planeta,Episodio):
         self.Nom = Nom
         self.Altura = Altura
         self.Edad = Edad
         self.Genero = Genero
         self.Especie = Especie
         self.Planeta = Planeta
         self.Episodio = Episodio

    
     def __str__(self):
         return f"{self.Nom} -{self.Altura},  {self.Edad}- {self.Genero},  {self.Especie}- {self.Planeta},  {self.Episodio}"

Datos_Personajes = [
    Personajes(Nom = "Juan ",Altura = 0.30, Edad = 900, Genero = "Femenino",Especie = "Droide",Planeta = "",Episodio = 4 ),
    Personajes(Nom = "Darth Vader",Altura = 1.40,  Edad = 500, Genero = "Masculino",Especie = "Humano",Planeta = "Alderaan" ,Episodio = 7),
    Personajes(Nom = "Han Solo",Altura = 0.40, Edad = 1000, Genero = "Femenino",Especie = "Droide",Planeta = "Alderaan" ,Episodio = 3),
    Personajes(Nom = "Chewbacca",Altura = 0.30, Edad = 476, Genero = "Masculino",Especie = "Humano",Planeta = "Alderaan" ,Episodio = 7),
    Personajes(Nom = "Clowd",Altura = 1.70, Edad = 476, Genero = "Masculino",Especie = "Humano",Planeta = "" ,Episodio = 5),
    ]

Lista_1 =List(Datos_Personajes)

def Femeninos():
    print("Personajes de genero femenino: ")
    for i in range(len(Lista_1)):
        if Lista_1[i].Genero == ("Femenino"):
            print(Lista_1[i].Nom)


def Droide():
    print("Droides que aparecieron mas en menos de 6 cap: ")
    for i in range(len(Lista_1)):
        if Lista_1[i].Especie == ("Droide"):
            if Lista_1[i].Episodio < 6:
                print(Lista_1[i].Nom)

def Mostrar_info():
    for i in range(len(Lista_1)):
        if Lista_1[i].Nom == ("Darth Vader"):
            print(Lista_1[i]) 
        if Lista_1[i].Nom == ("Han Solo"):
            print(Lista_1[i]) 

def Siete():
    print("Personajes que aparecieron el episodio 7: ")
    for i in range(len(Lista_1)):
        if Lista_1[i].Episodio == 7:
            print(Lista_1[i].Nom)

def Mayor():
    print("Personajes de mas de 850 años")
    for i in range(len(Lista_1)):
        if Lista_1[i].Edad > 850:
            print(Lista_1[i].Nom)

def Eliminar():
     print("Personajes eliminados")
     for i in range(len(Lista_1) - 1, -1, -1):
            if (Lista_1[i].Episodio == 4) or (Lista_1[i].Episodio == 5) or (Lista_1[i].Episodio == 6):
                print(Lista_1[i])
                Lista_1.pop(i)

def Humana():
    print("Humanos de Alderaan: ")
    for i in range(len(Lista_1)):
        if (Lista_1[i].Especie == ("Humano")) and  Lista_1[i].Planeta == ("Alderaan"):
            print(Lista_1[i].Nom)

def Menor():
    print("Personajes menores de 70 centimetros")
    for i in range(len(Lista_1)):
        if Lista_1[i].Altura <= 0.70:
            print(Lista_1[i].Nom)  

def Chewbacca():
    print("Chewbacca aparece en: ")
    for i in range(len(Lista_1)):
        if Lista_1[i].Nom == ("Chewbacca"):
            print(Lista_1[i].Episodio)  

Femeninos()
Droide()
Mostrar_info()
Siete()
Mayor()
Eliminar()
Lista_1.show()
Humana()
Menor()
Chewbacca()
from Cola import Cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido
import random


class Superheroes:
    def __init__(self, Nombre,Superheroe,Genero):
        self.Nombre = Nombre  # cambiamos a 'caracteres' para que coincida con _str_
        self.Superheroe = Superheroe
        self.Genero = Genero


    def __str__(self):
        return f"{self.Nombre}-{self.Superheroe} - {self.Genero}"
    
Datos = [
    Superheroes(Nombre = "Linterna Verde",Superheroe = "", Genero = "Femeninos"),
    Superheroes(Nombre = "Wolverine",Superheroe = 1934, Genero = "Hombre"),
    Superheroes(Nombre = "Dr Strange",Superheroe = "Capitan Marvel", Genero = "Femeninos"),
    Superheroes(Nombre = "Capitana Marvel",Superheroe = "Scott_Lang", Genero = "Hombre"),
    Superheroes(Nombre = "Mujer Maravilla",Superheroe = 1943, Genero = "Femeninos"),
    Superheroes(Nombre = "Flash",Superheroe = 1986, Genero = "Hombre"),
    Superheroes(Nombre = "Star-Lord",Superheroe = 1920, Genero = "Femeninos"),
    ]

Cola_1 = Cola()

for heroe in Datos:
    arribo(Cola_1, heroe)


def Capitan_Marvel():
    aux = Cola()
    while not cola_vacia(Cola_1):
        dato = atencion(Cola_1)
        arribo(aux,dato)
        if dato.Superheroe == ("Capitan Marvel"):
            print("El nombre de capitana marvel se llama: ",dato.Nombre)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))

def Femeninos():
    aux = Cola()
    print("Personajes Femeninos: ")
    while not cola_vacia(Cola_1):
      dato = atencion(Cola_1)
      arribo(aux,dato)
      if dato.Genero == ("Femeninos"):
          print(dato.Nombre)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))

def Masculino():
    aux = Cola()
    print("Personajes Masculino: ")
    while not cola_vacia(Cola_1):
      dato = atencion(Cola_1)
      arribo(aux,dato)
      if dato.Genero == ("Hombre"):
          print(dato.Nombre)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))

def Scott_Lang():
    aux = Cola()
    while not cola_vacia(Cola_1):
        dato = atencion(Cola_1)
        arribo(aux,dato)
        if dato.Superheroe == ("Scott_Lang"):
            print("El nombre de Scott_Lang se llama: ",dato.Nombre)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))          
          

barrido(Cola_1)
Capitan_Marvel()
Femeninos()
Masculino()
Scott_Lang()

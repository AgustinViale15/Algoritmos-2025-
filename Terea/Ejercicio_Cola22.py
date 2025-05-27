from Cola import Cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

Cola_1 = Cola()
Cola_2 = Cola()
Cola_3 = Cola()
Cola_F = Cola()
Cola_M = Cola()


class Datos_Cola:
    def __init__(self, Personaje,Superheroe,Genero):
        self.Personaje = Personaje
        self.Superheroe = Superheroe
        self.Genero = Genero


    def __str__(self):
        return str(self.Personaje)
        return str(self.Superheroe)
        return str(self.Genero)

def Cargar():    
    Cant = int(input("Ingrese cantidad de personajes: "))
    for i in range(Cant):
        Pers = input("Ingrse nombre del personaje: ")
        Super = input("Ingrse nombre del superhéroe: ")
        Genero = input("Ingrse género: ")
        Elem = Datos_Cola(Pers,Super,Genero)
        arribo(Cola_1,Elem)

def Capitana_Marvel():
    aux = Cola()
    while not cola_vacia(Cola_1):
        dato = atencion(Cola_1)
        if dato.Superheroe.lower() == "capitana marvel":
            print("Nombre de Capitana Marvel:", dato.Personaje)
        arribo(Cola_2, dato)
        arribo(aux, dato)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))

def Personajes_F():
    aux = Cola()
    while not cola_vacia(Cola_2):
        dato = atencion(Cola_2)
        if dato.Genero.upper() == "F":
            arribo(Cola_F, dato)
        arribo(aux, dato)
    while not cola_vacia(aux):
        arribo(Cola_2, atencion(aux))  


def Personajes_M():
    aux = Cola()
    while not cola_vacia(Cola_1):
        dato = atencion(Cola_1)
        if dato.Genero.upper() == "M":
            arribo(Cola_M, dato)
        arribo(aux, dato)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))  


def Scott_Lang():
    aux = Cola()
    while not cola_vacia(Cola_2):
        dato = atencion(Cola_2)
        if dato.Personaje.lower() == "scott lang":
            print("Nombre de Scott Lang es:", dato.Superheroe)
        arribo(aux, dato)
    while not cola_vacia(aux):
        arribo(Cola_2, atencion(aux))

def Personajes_S():
    aux = Cola()
    while not cola_vacia(Cola_2):
        dato = atencion(Cola_2)
        if dato.Personaje.lower().startswith('s') or dato.Superheroe.lower().startswith('s'):
            arribo(aux, dato)
    while not cola_vacia(aux):
        arribo(Cola_2, atencion(aux))

def Carol_Danvers():
    aux = Cola()
    encontrado = False
    while not cola_vacia(Cola_1):
        dato = atencion(Cola_1)
        if dato.Personaje.lower() == "carol danvers":
            print("Carol Danvers se encuentra")
            print("Nombre del superhéroe:", dato.Superheroe)
            encontrado = True
        arribo(aux, dato)
    while not cola_vacia(aux):
        arribo(Cola_1, atencion(aux))
    if not encontrado:
        print("Carol Danvers no se encuentra.")



Cargar()
Capitana_Marvel()
Personajes_F()
print("Superhéroes femeninos: ")
barrido(Cola_F)
Personajes_M()
print("Superhéroes masculinos:")
barrido(Cola_M)
Scott_Lang()
Personajes_S()
print("Personajes que comienzan con la letra S: ")
barrido(Cola_2)
Carol_Danvers()



           
        



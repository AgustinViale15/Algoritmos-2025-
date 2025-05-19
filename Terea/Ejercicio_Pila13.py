from Stack import Stack

Pila = Stack()
Pila_Nueva = Stack()
Lista = []
class Trajes:                                           # Declaracion
    def __init__(self, Modelo, Pelicula,Estado):
        self.Modelo = Modelo
        self.Pelicula = Pelicula
        self.Estado = Estado

    def __str__(self):
        return f"{self.Modelo} de {self.Pelicula} de {self.Estado}"

def Cargar_Valores():
    Valor = int(input("Ingresar cantidad de trajes: "))         #Cargo los datos
    for i in range(Valor):
        Mod = input("Ingresar modelo:  ")
        Pel = input("Ingresar pelicula en el que aparece:  ")
        Est = input("Ingresar estado de la armadura:  ")
        Trajes_Usados = Trajes(Mod,Pel,Est)
        Pila.push(Trajes_Usados)                            # Cargo los datos a la pila



def Pasar_Valores ():
    while Pila.size() > 0:
        Sale = Pila.pop()
        Pila_Nueva.push(Sale)
        Lista.append(Sale)                          #Paso los datos de la pila a una lista


def Mostrar_Lista():
    for i in range(len(Lista)):                     #Muestro los datos de la lista
        print(" ",i)
        print("Modelo: ",Lista[i].Modelo)
        print("Pelicula: ",Lista[i].Pelicula)
        print("Estado: ",Lista[i].Estado)

def Modelo_Mark_XLIV():
    Valor = 0
    for i in range(len(Lista)):                 # Punto A
        if Lista[i].Modelo == ("Mark XLIV"):
            Valor = 1

    if Valor == 1:
            print("La armadura Mark XLIV fue utilizado en la pelicula:",Lista[i].Pelicula)
    else:
            print("La armadura Mark XLIV no fue utilizado en alguna de las películas")


def Modelos_Dañados():
    for i in range(len(Lista)):
        if Lista[i].Estado == ("Dañado"):
            print("Modelos dañados: ",Lista[i].Modelo)


def Modelos_Destruidos():
    for traje in Lista[:]:      # VER
        if traje.Estado == ("Destruido"):
            print("Modelos destruidos: ",traje.Modelo)
            Lista.remove(traje)


def Agregar_Armadura():
    res = input("Desea agregar una armadura S/N: ")     # Punto E
    if res == ("S"):
        nueva = input("Ingrese nueva armadura: ")
        nueva_peli = input("Ingrese peli en la que aparece: ")
        nuevo_estado = input("Ingresar estado de la armadura: ")
        for i in range(len(Lista)):
            if (Lista[i].Modelo == nueva) and (Lista[i].Pelicula == nueva_peli):
                print("La armadura ",nueva, " ya aparece en la peli:  ",nueva_peli)
                break
            else:  
                Nuevo_Traje = Trajes(nueva,nueva_peli,nuevo_estado)   
                Pila_Nueva.push(Nuevo_Traje)
                print("La armadura ",nueva, " se agrego correctamente a la pila")
                break

def Trajes_Usados_en_Pelis():
    for i in range(len(Lista)):   # Punto F
        if (Lista[i].Pelicula == ("Spider-Man: Homecoming")) or (Lista[i].Pelicula == ("Capitan America: Civil War")):
            print("La armadura ",Lista[i].Modelo, " aparece en la peli: ",Lista[i].Pelicula)

Cargar_Valores()
Pasar_Valores()
Modelos_Dañados()
Modelos_Destruidos()
Agregar_Armadura()
Trajes_Usados_en_Pelis()
Modelo_Mark_XLIV()

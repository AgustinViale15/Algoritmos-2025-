from Stack import Stack
Pila = Stack()
Pila_Nueva = Stack()
Pila_Nueva1 = Stack()
Lista = []

class Personajes:
    def __init__(self,Nombre,Cantidad):
        self.Nombre = Nombre
        self.Cantidad = Cantidad

class Pel:
    def __init__(self,Nombre,Cantidad):
        self.Nombre = Nombre
        self.Cantidad = Cantidad

def Cargar_Datos():
    Per = int(input("Ingresar cantidad de personajes "))
    for i in range(Per):
        Nom = input("Ingresar nombre: ")
        Cant = int(input("Cantidad de peliculas: "))
        Personajes_ = Personajes(Nom,Cant)
        Pila.push(Personajes_) 

def Pasar_Valores ():
    while Pila.size() > 0:
        Sale = Pila.pop()
        Pila_Nueva.push(Sale)
        Lista.append(Sale)                         #Paso los datos de la pila a una lista

def Mostrar_Lista():
    for i in range(len(Lista)):                     #Muestro los datos de la lista
        print(" ",i)
        print("Modelo: ",Lista[i].Nombre)
        print("Pelicula: ",Lista[i].Cantidad)
        

def Modelo():
    for i in range(len(Lista)):
        if Lista[i].Nombre == ("Rocket Raccoon"):
            print("Rocket Raccoon se encuentra en la posicion: ",i)    
        if Lista[i].Nombre == ("Groot"):
            print("Groot se encuentra en la posicion: ",i)    


def Peliculas ():
    for i in range(len(Lista)):
        if Lista[i].Cantidad >= 5 :
           Agreg = Lista[i].Nombre
           Agreg2 = Lista[i].Cantidad
           Agregar = Pel(Agreg,Agreg2)
           Pila_Nueva1.push(Agregar)

def Ver ():
    print("Personajes que participaron en más de 5 películas: ")
    while Pila_Nueva1.size() > 0:
         personaje = Pila_Nueva1.pop()
         print("", personaje.Nombre)
         print(" aparece: ", personaje.Cantidad, " veces")

def Viuda_Negra():
    for i in range(len(Lista)):
        if Lista[i].Nombre == ("Viuda Negra"):
            print("Viuda Negra aparecio en ", Lista[i].Cantidad, " peiliculas: ")


Cargar_Datos()
Pasar_Valores()
Mostrar_Lista()
Modelo()
Peliculas()
Ver()
Viuda_Negra()
#Pila_Nueva.show
#Pila_Nueva1.show



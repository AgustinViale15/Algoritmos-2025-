from Stack import Stack


Pila = Stack()
Pila_Aux = Stack()
Pila_Mayores5 = Stack()


Lista = []


class Personaje:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad



def cargar_datos():
    n = int(input("Ingrese cantidad de personajes: "))
    for i in range(n):
        nom = input("Nombre del personaje: ").strip()
        cant = int(input("Cantidad de películas: "))
        personaje = Personaje(nom, cant)
        Pila.push(personaje)



def pasar_valores():
    while Pila.size() > 0:
        sale = Pila.pop()
        Pila_Aux.push(sale)
        Lista.append(sale)



def mostrar_lista():
    for i in range(len(Lista)):
        print("\nPosición:", i)
        print("Nombre: ", Lista[i].nombre)
        print("Películas: ", Lista[i].cantidad)



def buscar_personajes():
    for i in range(len(Lista)):
        if Lista[i].nombre == "Rocket Raccoon":
            print("Rocket Raccoon está en la posición:", i + 1, "(tomando 1 la cima)")
        if Lista[i].nombre == "Groot":
            print("Groot está en la posición:", i + 1, "(tomando 1 la cima)")



def personajes_mas_de_5():
    for i in range(len(Lista)):
        if Lista[i].cantidad > 5:
            Pila_Mayores5.push(Lista[i])


def ver_mayores_5():
    print("\nPersonajes con más de 5 películas:")
    while Pila_Mayores5.size() > 0:
        pers = Pila_Mayores5.pop()
        print(f"{pers.nombre} : {pers.cantidad} películas")



def viuda_negra():
    for i in range(len(Lista)):
        if Lista[i].nombre == "Viuda Negra" or Lista[i].nombre == "Black Widow":
            print("\nViuda Negra participó en:", Lista[i].cantidad, "películas")



def nombres_con_CDG():
    print("\nPersonajes cuyos nombres empiezan con C, D o G:")
    for i in range(len(Lista)):
        inicial = Lista[i].nombre[0].upper()
        if inicial in ("C", "D", "G"):
            print("-", Lista[i].nombre)



cargar_datos()
pasar_valores()

print("\nPila COMPLETA ")
mostrar_lista()

print("\nRESULTADOS")
buscar_personajes()
personajes_mas_de_5()
ver_mayores_5()
viuda_negra()
nombres_con_CDG()

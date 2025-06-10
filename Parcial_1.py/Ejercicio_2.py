from Personajes import superheroes
from Lista import List
from Cola import Cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

Lista_SuperHeroes = List(superheroes)
Cola_1 = Cola()

def Listado_Ordenado():
    Lista_SuperHeroes.add_criterion("name", lambda x: x["name"])
    Lista_SuperHeroes.sort_by_criterion("name")

    print("Listado ordenado por nombre:")
    for personaje in Lista_SuperHeroes:
        print(f"- {personaje['name']} ({personaje['alias']})")


def Posicion():
    pos = Lista_SuperHeroes.search("The Thing", "name")
    pos_2 = Lista_SuperHeroes.search("Rocket Raccoon", "name")
    print("The Thing se encuentra en la posicion: ",pos)
    print("Rocket Raccoon se encuentra en la posicion: ",pos_2)


def Villanos():
    print("Villanos:")
    for personaje in superheroes:
        if personaje["is_villain"]:
            print(f"- {personaje['name']}")

def Pasar_Villanos_Cola():
    for personaje in superheroes:
        if personaje["is_villain"]:
            arribo(Cola_1,personaje)
    while not cola_vacia(Cola_1):
        personaje = atencion(Cola_1)
        if personaje["first_appearance"] < 1980:
            print(f"- {personaje['name']} ({personaje['alias']}) - Año: {personaje['first_appearance']}")

def Listado_Comienza():
   Lestras = ("BL","G","My","W")
   print("Personajes que comienzan con BL,G,My,W: ")
   for personaje in superheroes:
        nombre = personaje["name"]
        if nombre.startswith(Lestras):
            print(f"- {nombre} ")

def Listado_Ordenado_Nombre_Real():
    Lista_SuperHeroes.add_criterion("real_name", lambda x: x.get("real_name", "") or "")
    Lista_SuperHeroes.sort_by_criterion("real_name")

    print("\nListado ordenado por nombre real:")
    for personaje in Lista_SuperHeroes:
        print(f"- {personaje['real_name']} ({personaje['name']})")

def Listado_Ordenado_Fecha():
    Lista_SuperHeroes.add_criterion("first_appearance", lambda x: x["first_appearance"])
    Lista_SuperHeroes.sort_by_criterion("first_appearance")

    print("\nListado ordenado por fecha:")
    for personaje in Lista_SuperHeroes:
        print(f"- {personaje['first_appearance']} ({personaje['name']})")

def Cambiar_Nombre():
    Nuevo_Name = "Scott Lang"
    Lista_SuperHeroes.add_criterion("name", lambda x: x["name"])
    Lista_SuperHeroes.sort_by_criterion("name")
    
    pos = Lista_SuperHeroes.search("Ant Man", "name")  # Devuelve posición o None
    if pos is not None:
        Lista_SuperHeroes[pos]["name"] = Nuevo_Name
        print("Nombre cambiado correctamente.")

    for personaje in Lista_SuperHeroes:
        print(f"({personaje['name']})")

1
def Mostrar_por_palabras_bio():
    print("Personajes con time-traveling o suit en su biografía:")
    for personaje in Lista_SuperHeroes:
        bio = personaje["short_bio"].lower()  # convertir a minúsculas para búsqueda insensible a mayúsculas
        if "time-traveling" in bio or "suit" in bio:
            print(f"- {personaje['name']} : {personaje['short_bio']}")

def Eliminar():
    print("Personajes Eliminados: ")
    Dato_1 = Lista_SuperHeroes.delete_value("Electro", "name")
    if Dato_1:
        print(f"- {Dato_1['name']} ({Dato_1['alias']}) - Año: {Dato_1['first_appearance']}")

    Dato_2 = Lista_SuperHeroes.delete_value("Baron Zemo", "name")
    if Dato_2:
        print(f"- {Dato_2['name']} ({Dato_2['alias']}) - Año: {Dato_2['first_appearance']}")


def menu():
    while True:
        print("\nMENÚ DE OPCIONES")
        print("1 - Listado ordenado por nombre")
        print("2 - Posición de The Thing y Rocket Raccoon")
        print("3 - Mostrar villanos")
        print("4 - Villanos antes de 1980 (en cola)")
        print("5 - Personajes que comienzan con BL, G, My o W")
        print("6 - Listado ordenado por nombre real")
        print("7 - Listado ordenado por fecha")
        print("8 - Cambiar nombre de Ant Man a Scott Lang")
        print("9 - Mostrar personajes con 'time-traveling' o 'suit' en su biografía")
        print("10 - Eliminar Electro y Baron Zemo")
        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Listado_Ordenado()
        elif opcion == "2":
            Posicion()
        elif opcion == "3":
            Villanos()
        elif opcion == "4":
            Pasar_Villanos_Cola()
        elif opcion == "5":
            Listado_Comienza()
        elif opcion == "6":
            Listado_Ordenado_Nombre_Real()
        elif opcion == "7":
            Listado_Ordenado_Fecha()
        elif opcion == "8":
            Cambiar_Nombre()
        elif opcion == "9":
            Mostrar_por_palabras_bio()
        elif opcion == "10":
            Eliminar()
        elif opcion == "0":
            print("Fin")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

        input("\nENTER para continuar")





#Listado_Ordenado()
#Posicion()
#Villanos()
#Pasar_Villanos_Cola()
#Listado_Comienza()
#istado_Ordenado_Nombre_Real()
#Listado_Ordenado_Fecha()
#Cambiar_Nombre()
#Mostrar_por_palabras_bio()
#Eliminar()
menu()
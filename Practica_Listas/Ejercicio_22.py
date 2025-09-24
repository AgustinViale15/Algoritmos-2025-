from Lista import List

class Jedi:
    def __init__(self, nombre, maestros, colores_sable, especie, padawan_de=None):
        self.nombre = nombre
        self.maestros = maestros 
        self.colores_sable = colores_sable 
        self.especie = especie
        self.padawan_de = padawan_de

    def __str__(self):
        return f"{self.nombre}-{self.maestros} - {self.colores_sable}- {self.especie}- {self.padawan_de}"
    
Datos_Jedi = [
    Jedi(nombre="Ahsoka Tano", maestros=["Anakin Skywalker"], colores_sable=["verde", "blanco"], especie="Togruta", padawan_de="Anakin Skywalker"),
    Jedi(nombre="Kit Fisto", maestros=[], colores_sable=["verde"], especie="Nautolano"),
    Jedi(nombre="Yoda", maestros=[], colores_sable=["verde"], especie="Desconocida"),
    Jedi(nombre="Luke Skywalker", maestros=["Yoda", "Obi-Wan Kenobi"], colores_sable=["azul", "verde"], especie="Humana"),
    Jedi(nombre="Obi-Wan Kenobi", maestros=["Qui-Gon Jin"], colores_sable=["azul"], especie="Humana", padawan_de="Qui-Gon Jin"),
    Jedi(nombre="Anakin Skywalker", maestros=["Obi-Wan Kenobi"], colores_sable=["azul"], especie="Humana", padawan_de="Obi-Wan Kenobi"),
    Jedi(nombre="Qui-Gon Jin", maestros=["Count Dooku"], colores_sable=["verde"], especie="Humana"),
    Jedi(nombre="Mace Windu", maestros=[], colores_sable=["violeta"], especie="Humana"),
    Jedi(nombre="Aayla Secura", maestros=["Quinlan Vos"], colores_sable=["azul"], especie="Twi'lek"),
    Jedi(nombre="Depa Billaba", maestros=["Mace Windu"], colores_sable=["azul"], especie="Humana", padawan_de="Mace Windu"),
    Jedi(nombre="Plo Koon", maestros=[], colores_sable=["amarillo", "azul"], especie="Kel Dor"),
    Jedi(nombre="Barriss Offee", maestros=["Luminara Unduli"], colores_sable=["violeta"], especie="Mirialana", padawan_de="Luminara Unduli"),
    Jedi(nombre="Cal Kestis", maestros=["Jaro Tapal"], colores_sable=["azul"], especie="Humana"),
    Jedi(nombre="Asajj Ventress", maestros=["Count Dooku"], colores_sable=["rojo"], especie="Dathomiriana"),
    Jedi(nombre="Shaak Ti", maestros=[], colores_sable=["azul"], especie="Togruta"),
    Jedi(nombre="Kanan Jarrus", maestros=["Depa Billaba"], colores_sable=["azul"], especie="Humana", padawan_de="Depa Billaba"),
    Jedi(nombre="Ezra Bridger", maestros=["Kanan Jarrus"], colores_sable=["azul"], especie="Humana", padawan_de="Kanan Jarrus"),
    Jedi(nombre="Rey Skywalker", maestros=["Leia Organa", "Luke Skywalker"], colores_sable=["amarillo"], especie="Humana"),
]

Lista_Jedi = List(Datos_Jedi)

#A
Lista_Jedi.add_criterion("nombre", lambda x: x.nombre)
Lista_Jedi.add_criterion("especie", lambda x: x.especie)

def Nombre():
    print("Lista ordenada por nombre: ")
    lista_por_nombre = List(Lista_Jedi.copy())
    lista_por_nombre.sort_by_criterion("nombre")
    
    for i in range(len(lista_por_nombre)):
        print(f"  {lista_por_nombre[i].nombre}")

print("")
def Especie():
    print("\nLista ordenada por especie: ")
    lista_por_especie = List(Lista_Jedi.copy())
    lista_por_especie.sort_by_criterion("especie")
    
    for i in range(len(lista_por_especie)):
        print(f"  {lista_por_especie[i].especie}: {lista_por_especie[i].nombre}")

#B

def Mostrar_Ahsoka_Tano_Kit_Fisto():
    print("")
    indice = Lista_Jedi.search("Ahsoka Tano","nombre")
    indice_2 = Lista_Jedi.search("Kit Fisto","nombre")
    print("",Lista_Jedi[indice])
    print("",Lista_Jedi[indice_2])


#C
print("")
def ejercicio_c_padawans_busqueda():
    maestros = ["Yoda", "Luke Skywalker"]
    for maestro in maestros:
        print(f"\nPadawans de {maestro}:")
        encontrados = False
        
        for i in range(len(Lista_Jedi)):
            if Lista_Jedi[i].padawan_de == maestro:
                print(f"{Lista_Jedi[i].nombre}")
                encontrados = True
        
        if not encontrados:
            print(f"{maestro} no tuvo padawans conocidos")

#D
def Mostrar_Jedi():
    print("Mostrar los Jedi de especie humana y twi'lek")
    especies = ["Humana", "Twi'lek"]
    
    for especie_buscada in especies:
        print(f"\nJedi de especie {especie_buscada}:")
        encontrados = False
        
        for i in range(len(Lista_Jedi)):
            if Lista_Jedi[i].especie == especie_buscada:
                print(f"{Lista_Jedi[i].nombre}")
                encontrados = True
        
        if not encontrados:
            print(f"No se encontraron Jedi de especie {especie_buscada}")

#E
def Jedi_A():
    print("")
    print("Jedis que comiezan con A: ")
    for i in range(len(Lista_Jedi)):
        if Lista_Jedi[i].nombre[0] == ("A") :
            print(Lista_Jedi[i].nombre)

#F
def Sable_de_Luz():
    print("")
    print("Jedis que usaron sable de luz de más de un color: ")
    for i in range(len(Lista_Jedi)):
        if len(Lista_Jedi[i].colores_sable) > 1:
            print(Lista_Jedi[i].nombre)

#G
def Sable_de_Luz_Amarillo_Violeta():
    print("")
    print("Jedis que usaron sable de luz amarillo o violeta: ")
    for i in range(len(Lista_Jedi)):
        if "amarillo" in Lista_Jedi[i].colores_sable or "violeta" in Lista_Jedi[i].colores_sable:
            print(Lista_Jedi[i].nombre)


#H
def ejercicio_h_padawans_busqueda():
    maestros = ["Qui-Gon Jin", "Mace Windu"]
    for maestro in maestros:
        print(f"\nPadawans de {maestro}:")
        encontrados = False
        
        for i in range(len(Lista_Jedi)):
            if Lista_Jedi[i].padawan_de == maestro:
                print(f"{Lista_Jedi[i].nombre}")
                encontrados = True
        
        if not encontrados:
            print(f"{maestro} no tuvo padawans conocidos")




Nombre()
Especie()
Mostrar_Ahsoka_Tano_Kit_Fisto()
print("")
ejercicio_c_padawans_busqueda()
Mostrar_Jedi()
Jedi_A()
Sable_de_Luz()
Sable_de_Luz_Amarillo_Violeta()
ejercicio_h_padawans_busqueda()
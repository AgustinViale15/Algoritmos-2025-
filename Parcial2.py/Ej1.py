from typing import List, Dict, Any
from collections import Counter


from tree import BinaryTree



def generar_pokemons() -> List[Dict[str, Any]]:
    
    pokes: List[Dict[str, Any]] = []

    
    base_pokes = [
        {
            "number": 1,
            "name": "Bulbasaur",
            "types": ["planta", "veneno"],
            "weaknesses": ["fuego", "hielo", "volador", "psiquico"],
            "mega": False,
            "gigamax": False,
        },
        {
            "number": 4,
            "name": "Charmander",
            "types": ["fuego"],
            "weaknesses": ["agua", "tierra", "roca"],
            "mega": False,
            "gigamax": False,
        },
        {
            "number": 6,
            "name": "Charizard",
            "types": ["fuego", "volador"],
            "weaknesses": ["agua", "electrico", "roca"],
            "mega": True,
            "gigamax": True,
        },
        {
            "number": 25,
            "name": "Pikachu",
            "types": ["electrico"],
            "weaknesses": ["tierra"],
            "mega": False,
            "gigamax": True,
        },
        {
            "number": 94,
            "name": "Gengar",
            "types": ["fantasma", "veneno"],
            "weaknesses": ["tierra", "psiquico", "fantasma", "siniestro"],
            "mega": True,
            "gigamax": True,
        },
        {
            "number": 135,
            "name": "Jolteon",
            "types": ["electrico"],
            "weaknesses": ["tierra"],
            "mega": False,
            "gigamax": False,
        },
        {
            "number": 745,
            "name": "Lycanroc",
            "types": ["roca"],
            "weaknesses": ["agua", "planta", "lucha", "tierra", "acero"],
            "mega": False,
            "gigamax": False,
        },
        {
            "number": 697,
            "name": "Tyrantrum",
            "types": ["roca", "dragon"],
            "weaknesses": ["hielo", "lucha", "dragon", "hada", "tierra", "acero"],
            "mega": False,
            "gigamax": False,
        },
        {
            "number": 52,
            "name": "Magnemite",
            "types": ["electrico", "acero"],
            "weaknesses": ["fuego", "tierra", "lucha"],
            "mega": False,
            "gigamax": False,
        },
        {
            "number": 208,
            "name": "Steelix",
            "types": ["acero", "tierra"],
            "weaknesses": ["fuego", "agua", "lucha", "tierra"],
            "mega": True,
            "gigamax": False,
        },
        {
            "number": 607,
            "name": "Litwick",
            "types": ["fuego", "fantasma"],
            "weaknesses": ["agua", "tierra", "roca", "fantasma", "siniestro"],
            "mega": False,
            "gigamax": False,
        },
    ]

    pokes.extend(base_pokes)

    
    next_number = max(p["number"] for p in base_pokes) + 1

    tipos_posibles = ["normal", "agua", "planta", "fuego", "electrico",
                      "lucha", "veneno", "tierra", "roca", "psiquico",
                      "hielo", "bicho", "fantasma", "acero", "siniestro", "dragon"]

    import random
    random.seed(42)

    while len(pokes) < 50:
        n = next_number
        name = f"Pokemon{n}"

        t1 = random.choice(tipos_posibles)
        if random.random() < 0.3:
            t2 = random.choice(tipos_posibles)
            types = list({t1, t2})
        else:
            types = [t1]

        w1 = random.choice(tipos_posibles)
        if random.random() < 0.4:
            w2 = random.choice(tipos_posibles)
            weaknesses = list({w1, w2})
        else:
            weaknesses = [w1]

        mega = random.random() < 0.1
        gigamax = random.random() < 0.08

        pokes.append({
            "number": n,
            "name": name,
            "types": types,
            "weaknesses": weaknesses,
            "mega": mega,
            "gigamax": gigamax,
        })

        next_number += 1

    return pokes




 


#1 


def construir_arboles(pokemons: List[Dict[str, Any]]):
    
    arbol_nombre = BinaryTree()
    arbol_numero = BinaryTree()
    arbol_tipo = BinaryTree()   

    for p in pokemons:
        
        arbol_nombre.insert(p["name"], p)

       
        arbol_numero.insert(p["number"], p)

       
        for t in p["types"]:
            nodo_tipo = arbol_tipo.search(t)
            if nodo_tipo is None:
                
                arbol_tipo.insert(t, [p])
            else:
                nodo_tipo.other_values.append(p)

    return arbol_nombre, arbol_numero, arbol_tipo


pokemons = generar_pokemons()


arbol_nombre, arbol_numero, arbol_tipo = construir_arboles(pokemons)





#2


def mostrar_pokemon(p: Dict[str, Any]):
    print(f"{p['number']:>4} - {p['name']}")
    print(f"  Tipos: {', '.join(p['types'])}")
    print(f"  Debilidades: {', '.join(p['weaknesses'])}")
    print(f"  Mega evolución: {'Sí' if p['mega'] else 'No'}")
    print(f"  Gigamax: {'Sí' if p['gigamax'] else 'No'}")
    print()






def buscar_por_numero(arbol_numero: BinaryTree, numero: int):
    nodo = arbol_numero.search(numero)
    if nodo is None:
        print(f"No se encontró ningún Pokémon con número {numero}")
    else:
        mostrar_pokemon(nodo.other_values)


def buscar_por_nombre_proximidad(arbol_nombre: BinaryTree, fragmento: str):
    
    fragmento = fragmento.lower()

    resultados = []

    def _rec(root):
        if root is not None:
            _rec(root.left)
            if fragmento in root.value.lower():
                resultados.append(root.other_values)
            _rec(root.right)

    _rec(arbol_nombre.root)

    if not resultados:
        print(f"No se encontraron pokémon que coincidan con '{fragmento}'")
    else:
        print(f"Pokémon cuyo nombre contiene '{fragmento}':")
        print()
        for p in resultados:
            mostrar_pokemon(p)



#3


def mostrar_pokemons_de_tipo(arbol_tipo: BinaryTree, tipo: str):
    nodo = arbol_tipo.search(tipo)
    if nodo is None:
        print(f"No hay pokémon del tipo {tipo}")
    else:
        print(f"Pokémon del tipo {tipo}:")
        print()
        for p in nodo.other_values:
            print(p["name"])
        print()


#4


def listado_ordenado_por_numero(arbol_numero: BinaryTree):
    print("Listado por número (in-order):")
    print()

    def _in(root):
        if root is not None:
            _in(root.left)
            p = root.other_values
            print(f"{p['number']:>4} - {p['name']}")
            _in(root.right)

    _in(arbol_numero.root)
    print()


def listado_ordenado_por_nombre(arbol_nombre: BinaryTree):
    print("Listado por nombre (in-order):")
    print()

    def _in(root):
        if root is not None:
            _in(root.left)
            p = root.other_values
            print(f"{p['name']}  ({p['number']})")
            _in(root.right)

    _in(arbol_nombre.root)
    print()


def listado_por_nivel_nombre(arbol_nombre: BinaryTree):
   
    from collections import deque

    if arbol_nombre.root is None:
        print("Árbol vacío")
        return

    cola = deque()
    cola.append(arbol_nombre.root)
    nivel = 0

    print("Listado por nivel (por nombre):")
    print()

    while cola:
        nodos_nivel = len(cola)
        print(f"\nNivel {nivel}:")
        for _ in range(nodos_nivel):
            nodo = cola.popleft()
            p = nodo.other_values
            print(f"  {p['name']}  ({p['number']})")
            if nodo.left is not None:
                cola.append(nodo.left)
            if nodo.right is not None:
                cola.append(nodo.right)
        nivel += 1
    print()



#5


def pokemons_debiles_a(pokemons: List[Dict[str, Any]],
                       arbol_nombre: BinaryTree,
                       nombres_atacantes: List[str]):
    
    tipos_atacantes = set()

    for nombre in nombres_atacantes:
        nodo = arbol_nombre.search(nombre)
        if nodo is not None:
            tipos_atacantes.update(nodo.other_values["types"])

    print("Tipos de los atacantes:", ", ".join(tipos_atacantes))

    print("\nPokémon débiles frente a esos tipos:")
    print()

    for p in pokemons:
        if any(t in p["weaknesses"] for t in tipos_atacantes):
            print(f"{p['name']} ({p['number']}) es débil a alguno de: {', '.join(tipos_atacantes)}")
    print()



#6


def contar_pokemons_por_tipo(pokemons: List[Dict[str, Any]]):
    contador = Counter()

    for p in pokemons:
        for t in p["types"]:
            contador[t] += 1

    print("Cantidad de pokémon por tipo:")
    print()
    for tipo, cant in sorted(contador.items(), key=lambda x: x[0]):
        print(f"{tipo}: {cant}")
    print()



#7 y 8


def contar_mega_y_gigamax(pokemons: List[Dict[str, Any]]):
    mega = sum(1 for p in pokemons if p["mega"])
    giga = sum(1 for p in pokemons if p["gigamax"])

    print(f"Cantidad de pokémon con megaevolución: {mega}")
    print(f"Cantidad de pokémon con forma gigamax: {giga}")
    print()




print()
print("BUSCAR POR NÚMERO (ejemplo 25)")
print()
buscar_por_numero(arbol_numero, 25)



    
    
print()
print("BUSCAR POR NOMBRE (proximidad 'bul')")
print()
buscar_por_nombre_proximidad(arbol_nombre, "bul")

  
print()
print("POKÉMON POR TIPO")
print()
for tipo in ["fantasma", "fuego", "acero", "electrico"]:
    mostrar_pokemons_de_tipo(arbol_tipo, tipo)

 
print()
print("LISTADO ORDENADO POR NÚMERO")
print()
listado_ordenado_por_numero(arbol_numero)

print()
print("LISTADO ORDENADO POR NOMBRE")
print()
listado_ordenado_por_nombre(arbol_nombre)

print()
print("LISTADO POR NIVEL (POR NOMBRE)")
print()
listado_por_nivel_nombre(arbol_nombre)


print()
print("POKÉMON DÉBILES FRENTE A JOLTEON, LYCANROC Y TYRANTRUM")
print()
pokemons_debiles_a(pokemons, arbol_nombre,
                       ["Jolteon", "Lycanroc", "Tyrantrum"])

   
print()
print("CANTIDAD DE POKÉMON POR TIPO")
print()
contar_pokemons_por_tipo(pokemons)

  
print()
print("MEGAEVOLUCIÓN Y GIGAMAX")
print()
contar_mega_y_gigamax(pokemons)
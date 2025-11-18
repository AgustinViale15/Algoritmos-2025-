from graph import Graph   
from math import inf

#1 y 4

personajes = {
    "Luke Skywalker":  [1,2,3,4,5,6],
    "Darth Vader":     [1,2,3,5,6],
    "Yoda":            [1,2,3,5,6,8],
    "Boba Fett":       [2,5,6],
    "C-3PO":           [1,2,3,4,5,6,7,8,9],
    "Leia":            [1,2,3,4,5,6,7,8,9],
    "Rey":             [7,8,9],
    "Kylo Ren":        [7,8,9],
    "Chewbacca":       [1,2,3,4,5,6,7,8,9],
    "Han Solo":        [1,2,3,4,5,6,7],
    "R2-D2":           [1,2,3,4,5,6,7,8],
    "BB-8":            [7,8,9],
}



g = Graph(is_directed=False)


for p in personajes:
    g.insert_vertex(p)


def episodios_en_comun(lista1, lista2):
    return len(set(lista1).intersection(lista2))

nombres = list(personajes.keys())

for i in range(len(nombres)):
    for j in range(i+1, len(nombres)):
        p1 = nombres[i]
        p2 = nombres[j]
        cant = episodios_en_comun(personajes[p1], personajes[p2])

        if cant > 0:               
            g.insert_edge(p1, p2, cant)

#2

def mst_desde(grafo, personaje):
    print(f"\nÁrbol de Expansión Mínima desde: {personaje}")
    
    mst = grafo.kruskal(personaje)
    total = 0

    aristas = mst.split(";")

    for arista in aristas:
        partes = arista.split("-")
        if len(partes) != 3:
            continue   

        o, d, peso = partes
        peso = int(peso)

        print(f"{o} a {d} ({peso} episodios)")
        total += peso

    print(f"Peso total del árbol: {total} episodios\n")



mst_desde(g, "C-3PO")
mst_desde(g, "Yoda")
mst_desde(g, "Leia")

#3

def maximo_episodios_compartidos(g):
    max_peso = -1
    pares = []

    for v in g:
        for edge in v.edges:
            if edge.weight > max_peso:
                max_peso = edge.weight
                pares = [(v.value, edge.value)]
            elif edge.weight == max_peso:
                pares.append((v.value, edge.value))

    print("\nMáximo número de episodios compartidos:", max_peso)
    print("Pares de personajes:")
    for a, b in pares:
        print(f"  {a} y {b}")

maximo_episodios_compartidos(g)

#5

def dijkstra_2(grafo, origen, destino):
    pila = grafo.dijkstra(origen)
    camino = []
    actual = destino
    costo = None

    while pila.size() > 0:
        nombre, dist, previo = pila.pop()
        if nombre == actual:
            if costo is None:
                costo = dist
            camino.append(nombre)
            actual = previo
            if previo is None:
                break

    camino.reverse()
    return camino, costo



cam, cost = dijkstra_2(g, "C-3PO", "R2-D2")
print("\nCamino más corto de C-3PO a R2-D2:", cam, "Costo:", cost)


cam, cost = dijkstra_2(g, "Yoda", "Darth Vader")
print("Camino más corto de Yoda a Darth Vader:", cam, "Costo:", cost)

#6

print("\nPersonajes que aparecieron en TODOS los episodios (1-9):")
for p, eps in personajes.items():
    if len(set(eps)) == 9:
        print("  ", p)

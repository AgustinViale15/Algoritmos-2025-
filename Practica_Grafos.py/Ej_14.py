from typing import Any, Optional

from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack
class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any,tipo: str, other_values: Optional[Any] = None):
            self.value = value
            self.tipo = tipo
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            return self.value
    
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values 
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight
    
    def show(
        self
    ) -> None:
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insert_vertex(
        self,
        value: Any,
        tipo: str,
    ) -> None:
        node_vertex = Graph.__nodeVertex(value,tipo)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        delete_value = g.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    def deep_sweep(self, value) -> None:
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos].value)
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value)-> None:
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        while no_visited.size() > 0:
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if pos is not None:
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path
    

    def dijkstra_2(self, origin):
        from math import inf
        no_visited = HeapMin()
        path = Stack()

       
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            item = [vertex.value, vertex, None, distance]
            no_visited.arrive(item, distance)

        while no_visited.size() > 0:

            prioridad, datos = no_visited.attention()

            nombre_actual = datos[0]
            nodo_actual   = datos[1]
            previo        = datos[2]
            costo_actual  = datos[3]

            path.push([nombre_actual, costo_actual, previo])

            for edge in nodo_actual.edges:
                pos = no_visited.search(edge.value)
                if pos is not None:

                    nuevo_costo = costo_actual + edge.weight

                    
                    prioridad_destino, datos_destino = no_visited.elements[pos]
                    distancia_destino = datos_destino[3]

                    if nuevo_costo < distancia_destino:
                        datos_destino[2] = nombre_actual
                        datos_destino[3] = nuevo_costo
                        no_visited.change_priority(pos, nuevo_costo)

        return path



    def kruskal(self, origin_vertex=None):

    
        def find_set(forest, value):
            for i, group in enumerate(forest):
                if value in group:
                    return i
            return None

        forest = []     
        edges = HeapMin()

        
        for vertex in self:
            forest.append({vertex.value})   

            
            for edge in vertex.edges:
                
                if vertex.value < edge.value:
                    edges.arrive([vertex.value, edge.value], edge.weight)

        mst = []  

        
        while edges.size() > 0 and len(forest) > 1:
            peso, (origen, destino) = edges.attention()

            i = find_set(forest, origen)
            j = find_set(forest, destino)

            if i != j:
               
                mst.append((origen, destino, peso))

               
                forest[i] = forest[i].union(forest[j])
                forest.pop(j)

        return mst
    

def camino_minimo(grafo, origen, destino):
    pila = grafo.dijkstra_2(origen)
    camino = []
    actual = destino
    costo_total = None

    while pila.size() > 0:
        nombre, costo, previo = pila.pop()

        if nombre == actual:
            if costo_total is None:
                costo_total = costo

            camino.append(nombre)
            actual = previo

            if previo is None:
                break

    if not camino:
        return None, None

    camino.reverse()
    return camino, costo_total





g = Graph(is_directed=False)


# A


g.insert_vertex("Cocina", "ambiente")
g.insert_vertex("Comedor", "ambiente")
g.insert_vertex("Cochera", "ambiente")
g.insert_vertex("Quincho", "ambiente")
g.insert_vertex("Baño 1", "ambiente")
g.insert_vertex("Baño 2", "ambiente")
g.insert_vertex("Habitación 1", "ambiente")
g.insert_vertex("Habitación 2", "ambiente")
g.insert_vertex("Sala de estar", "ambiente")
g.insert_vertex("Terraza", "ambiente")
g.insert_vertex("Patio", "ambiente")


# B



g.insert_edge("Cocina", "Comedor", 4)
g.insert_edge("Cocina", "Baño 1", 6)
g.insert_edge("Cocina", "Terraza", 8)
g.insert_edge("Cocina", "Sala de estar", 10)
g.insert_edge("Cocina", "Habitación 1", 12)


g.insert_edge("Sala de estar", "Comedor", 5)
g.insert_edge("Sala de estar", "Habitación 2", 7)
g.insert_edge("Sala de estar", "Patio", 9)
g.insert_edge("Sala de estar", "Baño 2", 6)
g.insert_edge("Sala de estar", "Terraza", 11)


g.insert_edge("Comedor", "Baño 1", 3)
g.insert_edge("Comedor", "Habitación 1", 7)
g.insert_edge("Comedor", "Cochera", 9)

g.insert_edge("Cochera", "Patio", 10)
g.insert_edge("Cochera", "Quincho", 14)
g.insert_edge("Cochera", "Habitación 2", 12)

g.insert_edge("Patio", "Quincho", 8)
g.insert_edge("Patio", "Terraza", 15)
g.insert_edge("Patio", "Baño 2", 6)

g.insert_edge("Quincho", "Baño 1", 11)
g.insert_edge("Quincho", "Habitación 2", 10)
g.insert_edge("Quincho", "Terraza", 9)

g.insert_edge("Baño 1", "Baño 2", 4)
g.insert_edge("Baño 1", "Habitación 1", 6)
g.insert_edge("Baño 1", "Habitación 2", 5)

g.insert_edge("Baño 2", "Habitación 1", 8)
g.insert_edge("Baño 2", "Habitación 2", 7)

g.insert_edge("Habitación 1", "Habitación 2", 6)
g.insert_edge("Habitación 1", "Terraza", 13)

g.insert_edge("Habitación 2", "Terraza", 7)



# C

print("")
mst = g.kruskal()

print("Árbol de expansión mínima:")
total_metros = 0

for o, d, p in mst:
    print(f"{o} -- {d}   ({p} m)")
    total_metros += p

print(f"Total de cable necesario para conectar TODA la casa: {total_metros} metros")



# D

print("")
camino, costo = camino_minimo(g, "Habitación 1", "Sala de estar")

print("Camino más corto desde Habitación 1 hasta Sala de estar:")
print("Ruta:", camino)
print(f"Metros de cable necesarios: {costo} m")


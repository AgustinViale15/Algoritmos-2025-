from tree import BinaryTree
from random import choice

# Crear el árbol
arbol_binario_Nombre = BinaryTree()
arbol_binario_Heroes = BinaryTree()
arbol_binario_Villanos = BinaryTree()

# Lista de personajes (corregí algunos nombres que parecían de otras sagas)
Personajes_MCU = [
    "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow",
    "Hawkeye", "Thanos", "Loki", "Ultron", "Red Skull",
    "Black Panther", "Docto Strange", "Spider-Man", "Star-Lord",
    "Gamora", "Rocket", "Groot", "Drax", "Nebula"
]

for nombre_personaje in Personajes_MCU:
    info = {
        "es_heroe": choice([True, False])  # Esto asignará aleatoriamente
        # Si quieres asignar específicamente, deberías hacerlo manualmente
    }
    arbol_binario_Nombre.insert(nombre_personaje, info)

#B
print()
print("Listado de villanos ordenado alfabéticamente:")
arbol_binario_Nombre.in_order_Villanos()

#C
print()
print("Superheroes con C:")
arbol_binario_Nombre.in_order_C()

#D
print()
arbol_binario_Nombre.in_order_heroes()

#E
print("")
print("Modifico a Docto Strange")
pos = arbol_binario_Nombre.search("Docto Strange") 

if pos is not None:
   info2 = pos.other_values.copy()

arbol_binario_Nombre.delete("Docto Strange")
arbol_binario_Nombre.insert("Doctor Strange", info2)
arbol_binario_Nombre.in_order()

#F
print("")
print("Arbol desendente de heroes")
arbol_binario_Nombre.post_order_Heroes()

#G

def in_order_Bosque(self,arbol_binario_Heroes,arbol_binario_Villanos):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value,root.other_values)
                if root.other_values.get("es_heroe") == True:
                     arbol_binario_Heroes.insert(root.value, root.other_values.copy())
                else:
                     arbol_binario_Villanos.insert(root.value, root.other_values.copy())
                     
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

in_order_Bosque(arbol_binario_Nombre, arbol_binario_Heroes,arbol_binario_Villanos)


print("")
print("Arbol de heroes:")
arbol_binario_Heroes.in_order()

print("")
print("Arbol de villanos:")
arbol_binario_Villanos.in_order()


#I
print("")
print("Nodos heroes: ")
arbol_binario_Heroes.in_order_nodos()
print("Nodos villanos: ")
arbol_binario_Villanos.in_order_nodos()

#II
print()
print("Arbol de heroes ordenado alfabéticamente: ")
arbol_binario_Heroes.in_order()
print()
print("Arbol de villanos ordenado alfabéticamente: ")
arbol_binario_Villanos.in_order()
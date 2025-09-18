#Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas
#a un archivo que contiene personajes de la saga de Star Wars, de los cuales se sabe su nombre,
#altura y peso. Además deberá contemplar los siguientes requerimientos:
#a. en el árbol se almacenara solo el nombre del personaje, además de la posición en la que se
#encuentra en el archivo (nrr);
#b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo
#de baja;
#c. mostrar toda la información de Yoda y Boba Fett;
#d. mostrar un listado ordenado alfabéticamente de los personajes que miden más de 1 metro;

#e. mostrar un listado ordenado alfabéticamente de los personajes que pesan menos de 75 ki-
#los;

#f. deberá utilizar el TDA archivo desarrollado en el capítulo V;

from tree import BinaryTree
arbol_binario = BinaryTree()
arbol_binario_Id = BinaryTree()

Personajes = (("Yoda",1),("Lucas",2),("Cle",3),("Cloud",4),("Boba Fett",8) )
from random import randint
for Personajes in Personajes:
    info = {
        "Peso": randint(10,100),
        "Altura": randint(60,200),
        
    }
    info.update({"Id":Personajes[1]})
    arbol_binario.insert(Personajes[0], info)

    info2 = info.copy()
    info2.pop("Id")
    info2.update({"name":Personajes[0]})
    arbol_binario_Id.insert(Personajes[1],info2)

arbol_binario.in_order()

#B


print("Agrego: San")
arbol_binario.insert("San", {"Peso":100, "Altura":175, "Id":15})
arbol_binario_Id.insert(15, {"Peso":100, "Altura":175, "name":"San"})
arbol_binario.in_order()
arbol_binario_Id.in_order()
print(" Elimino San")
value, other_value = arbol_binario.delete("San")
arbol_binario_Id.delete(other_value["Id"])
arbol_binario.in_order()
arbol_binario_Id.in_order()


print("Modifico a Cloud")
pos = arbol_binario.search("Cloud") 
if pos is not None:
    pos.other_values["Peso"] = 115
    pos.other_values["Altura"] = 71

arbol_binario.in_order()






#4

#C
pos =arbol_binario.search("Yoda")
if pos is not None:
    print(f'serch character {pos.value}, character info {pos.other_values}')

pos =arbol_binario.search("Boba Fett")
if pos is not None:
    print(f'serch character {pos.value}, character info {pos.other_values}')

#D
print("Personajes mayores a 100Cm: ")
arbol_binario.in_order_height()
#E
print("Personajes menores de 75kg: ")
arbol_binario.in_order_peso()

arbol_binario_Id.in_order()
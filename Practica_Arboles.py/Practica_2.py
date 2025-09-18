import random
from typing import Any, Optional

class Arbol_Binaro:

    class __Nodo_Arbol:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return Arbol_Binaro.__Nodo_Arbol(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)
     
    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)


    def search(self, value: Any) -> __Nodo_Arbol:
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux
    
    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values

        


arbol = Arbol_Binaro()

for i in range(10):
     arbol.insert(random.randint(1,100))


print("\nRecorrido post-order:")
arbol.post_order()

Res = int(input("Ingrese valor a buscar: "))

arbol.search(Res)

if arbol.search(Res) is not None:
    print("Numero encontrado")
else:
    print("Numero No encoentrado")

print ("Ingresar elementos a eliminar: ")
Num1 = int(input("Ingrese valor a eliminar: "))
Num2 = int(input("Ingrese valor a eliminar: "))
Num3 = int(input("Ingrese valor a eliminar: "))

arbol.delete(Num1)
arbol.delete(Num2)
arbol.delete(Num3)

print("Arbol con 3 elementos borrados: ")
arbol.post_order()
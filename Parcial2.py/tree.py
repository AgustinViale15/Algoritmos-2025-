from typing import Any, Optional
from queue_ import Queue
from collections import Counter

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.hight = 0

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_hight(root)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value,root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value,root.other_values)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any) -> __nodeTree:
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

    def proximity_search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

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

                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def hight(self, root):
        if root is None:
            return -1
        else:
            return root.hight

    def update_hight(self, root):
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_hight(root)
        self.update_hight(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control: # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.hight(root.left) - self.hight(root.right) == 2:
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.hight(root.right) - self.hight(root.left) == 2:
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root

    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)

    def count_heroes(self):
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        
        return total
    
    def divide_tree(self, arbol_h, arbol_v):
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)


        __divide_tree(self.root, arbol_h, arbol_v)

    

    def in_order_height(self):
        def __in_order_height(root):
            if root is not None:
                __in_order_height(root.left)
                if root.other_values['Altura'] > 100:
                    print(root.value, root.other_values['Altura'])
                __in_order_height(root.right)

        if self.root is not None:
            __in_order_height(self.root)
    
    def in_order_peso(self):
        def __in_order_peso(root):
            if root is not None:
                __in_order_peso(root.left)
                if root.other_values['Peso'] < 75:
                    print(root.value, root.other_values['Peso'])
                __in_order_peso(root.right)

        if self.root is not None:
            __in_order_peso(self.root)
    
    def in_order_Villanos(self):
        def __in_order_Villanos(root):
            if root is not None:
                __in_order_Villanos(root.left)
                if root.other_values.get("es_heroe") == False: 
                    print(root.value,root.other_values)

                __in_order_Villanos(root.right)

        if self.root is not None:
            __in_order_Villanos(self.root)



    def in_order_C(self):
        def __in_order_C(root):
            if root is not None:
                __in_order_C(root.left)
                if root.value[0] == ("C"):
                    print(root.value,root.other_values)

                __in_order_C(root.right)

        if self.root is not None:
            __in_order_C(self.root)

    def in_order_heroes(self):
        cont = 0
        def __in_order_heroes(root):
            nonlocal cont
            if root is not None:
                __in_order_heroes(root.left)
                if root.other_values.get("es_heroe") == True:
                    cont += 1
                
                __in_order_heroes(root.right)

        
        if self.root is not None:
            __in_order_heroes(self.root)
        print("Cantidad de superheroes: ",cont)
    

    def in_order_nodos(self):
        cont = 0
        def __in_order(root):
            nonlocal cont
            if root is not None:
                __in_order(root.left)
                cont += 1

                
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)
        print("Cantidad de nodos: ",cont)

    def post_order_Heroes(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                if root.other_values.get("es_heroe") == True:
                    print(root.value,root.other_values)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def in_order_Ej_23(self):
        def __in_order_Ej_23(root):
            if root:
                __in_order_Ej_23(root.left)
                print(f"Criatura: {root.value}, derrotado por: {root.other_values}")
                __in_order_Ej_23(root.right)
        
        if self.root:
            __in_order_Ej_23(self.root)



    def in_order_derrotas(self):
        
        
        derrotadores = []
        
        def __in_order_derrota(root):
            if root is not None:
                __in_order_derrota(root.left)
                if root.other_values is not None and root.other_values != "-":
                    derrotadores.append(root.other_values)
                __in_order_derrota(root.right)
        
        __in_order_derrota(self.root)
        
        contador = Counter(derrotadores)
        
        top_3 = contador.most_common(3)
        
        
        
        for i, (derrotador, cantidad) in enumerate(top_3, 1):
            print(f"{i}. {derrotador}: {cantidad} criatura(s) derrotada(s)")
        
        return top_3
    
    
    
    def in_order_Heracles(self):
        criaturas_derrotadas = []
        
        def __in_order_Heracles(root):
            if root is not None:
                __in_order_Heracles(root.left)
                if root.other_values is not None and root.other_values == "Heracles":
                    criaturas_derrotadas.append(root.value)
                __in_order_Heracles(root.right)
        
        __in_order_Heracles(self.root)
        
        
        
        if criaturas_derrotadas:
            print(f"Heracles derrotó a {len(criaturas_derrotadas)} criaturas:")
            for i, criatura in enumerate(criaturas_derrotadas, 1):
                print(f"{i}. {criatura}")
        else:
            print("Heracles no derrotó a ninguna criatura en la lista.")
        
        return criaturas_derrotadas


    def in_order_no_derrotas(self):
        
        
        derrotadores = []
        
        def __in_order_no_derrotas(root):
            if root is not None:
                __in_order_no_derrotas(root.left)
                if root.other_values == "-":
                    derrotadores.append(root.value)
                __in_order_no_derrotas(root.right)
        
        __in_order_no_derrotas(self.root)
        
        if derrotadores:
            print(f"Criaturas no derrotadas {len(derrotadores)} :")
            for i, criatura in enumerate(derrotadores, 1):
                print(f"{i}. {criatura}")
        
        return derrotadores
    
    def search_by_partial_match(self, partial_name):
        "Busca criaturas que contengan el texto partial_name en su nombre"
        results = []
        
        def __search_partial(root, partial):
            if root is not None:
                __search_partial(root.left, partial)
                
                if partial.lower() in root.value.lower():
                    results.append(root)
                
                __search_partial(root.right, partial)
        
        __search_partial(self.root, partial_name)
        return results
    

    def listar_por_nivel(self):
        "Recorrido por nivel "
        if self.root is None:
            print("El árbol está vacío")
            return
        
        from collections import deque
        cola = deque()
        cola.append(self.root)
        nivel_actual = 0
        
        print("Listado por Nivel")
        
        while cola:
            nodos_en_nivel = len(cola)
            print(f"\n Nivel {nivel_actual} ")
            
            for i in range(nodos_en_nivel):
                nodo = cola.popleft()
                
                print(f"Criatura: {nodo.value}, Derrotado por: {nodo.other_values}")
                
                if nodo.left is not None:
                    cola.append(nodo.left)
                if nodo.right is not None:
                    cola.append(nodo.right)
            
            nivel_actual += 1

    def in_order_Heracles(self):
        def __in_order_Heracles(root):
            if root is not None:
                __in_order_Heracles(root.left)
                if root.other_values == ("Heracles"):
                    print(root.value)
                __in_order_Heracles(root.right)

        if self.root is not None:
            __in_order_Heracles(self.root)

    

    

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()




# print()K
# arbol.update_hight(arbol.root.left.left)
# print()
# arbol.update_hight(arbol.root.left)
# print()
# arbol.update_hight(arbol.root)
# print()
# arbol.pre_order()

# arbol.insert('F', 'f')
# arbol.insert('B', 'b')
# arbol.insert('K', 'k')
# arbol.insert('H', 'h')
# arbol.insert('J', 'j')
# arbol.insert('E', 'e')
# arbol.insert('B')
# arbol.insert('V')
# arbol.pre_order()
# print()

#for i in range(1, 16):
#    arbol.insert(i)

#arbol.pre_order()

# if pos is not None:
#     arbol.delete('F')
#     arbol.insert('C', 'c')

# delete_value, deleter_other_values = arbol.delete('K')
# if delete_value is not None:
#     print(delete_value, deleter_other_values)


# arbol.in_order()
# # delete_value = arbol.delete('F')

# # if delete_value is not None:
# #     print(f'valor eliminado {delete_value}')
# # else:
# #     print('valor no encontrado')
# # print()
# arbol.by_level()


# # arbol.insert(11)

# # pos = arbol.search(19)
# # print(pos)
# arbol.in_order()

# from super_heroes_data import superheroes

# for super_hero in superheroes:
#     arbol.insert(super_hero['name'], super_hero)


# arbol.divide_tree(arbol_heroes, arbol_villanos)

# bosque = [arbol_heroes, arbol_villanos]

# for tree in bosque:
#     tree.in_order()
#     print()

# arbol.proximity_search('Dr')
# name = input('ingrese nombre para modificar: ')
# value, other_value = arbol.delete(name)

# if value is not None:
#     fix_name = input('ingrese el nuevo nombre: ')
#     other_value['name'] = fix_name
#     arbol.insert(fix_name, other_value) 

# print()
# arbol.proximity_search('Dr')
# print()
# pos = arbol.search('Dr Strange')
# if pos is not None:
#     print(pos.value, pos.other_values)

# print(arbol.count_heroes())

# arbol.villain_in_order()

# print()
# pos = arbol.search("Thanos")
# if pos is not None:
#     print(pos.value, pos.other_values)
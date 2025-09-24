from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {} #Es un diccionario de funciones de criterio

    def add_criterion(self,key_criterion: str,function,):  #Permite registrar una nueva función de criterio bajo una clave
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None: #Imprime todos los elementos de la lista.
        for element in self:
            print(element)

    def delete_value(self,value, key_value: str = None, ) -> Optional[Any]:  #Busca value usando la búsqueda binaria.
        index = self.search(value, key_value)                                #Si lo encuentra, lo elimina con .pop(index) y lo retorna.
        return self.pop(index) if index is not None else index               #Si no lo encuentra, retorna None.

    # def insert_value(
    #     self,
    #     value: Any,
    # ) -> None:
    #     # list_number.append(2)
    #     # list_number.insert(1, 11)
    #     pass

    def sort_by_criterion(self,criterion_key: str = None,) -> None:     #Si se especifica un criterion_key, intenta usar la función registrada con ese nombre para ordenar.
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)         #Si no se especifica, y los elementos son básicos (números, strings, etc.), se ordenan naturalmente.
                                                                        #Si no puede ordenarlos, muestra un mensaje.
        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(self,search_value,search_key: str = None,) -> int:       #Realiza búsqueda binaria sobre la lista:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2
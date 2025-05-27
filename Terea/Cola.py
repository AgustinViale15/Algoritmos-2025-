class nodoCola():
    info,sig = None,None

class Cola():
    def __init__(self):  # ✔️ Constructor correcto
        self.frente, self.final = None, None
        self.tamanio = 0



def arribo(cola, dato):
    """Arriba el dato al final de la cola."""
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    """Atiende el elemento en el frente de la cola y lo devuelve."""
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato

def cola_vacia(cola):
    """Devuelve true si la cola está vacía."""
    return cola.frente is None

def en_frente(cola):
    """Devuelve el valor almacenado en el frente de la cola."""
    return cola.frente.info

def tamanio(cola):
    """Devuelve el número de elementos en la cola."""
    return cola.tamanio

def mover_al_final(cola):
    dato = atencion(cola)
    arribo(cola,dato)
    return dato

def barrido(cola):
    # MUestra el contenido de una cola sin perder datos
    caux = Cola()
    while (not cola_vacia(cola)):
        dato = atencion(cola)
        print(dato)
        arribo(caux,dato)
    while (not cola_vacia(caux)):
        dato = atencion(caux)
        arribo(cola,dato)
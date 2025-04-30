import random
from stack import Stack

Pila = Stack()
Pila_Espada = Stack()
Pila_Basto = Stack()
Pila_Oro = Stack()
Pila_Copa = Stack()
Pila_Ordenada = Stack()
Lista = []
Palos = ["Espada","Basto","Oro","Copa"]
Valores = [1,2,3,4,5,6,7,10,11,12]

class Carta:
    def __init__(self, Palo, Valor):
        self.Palo = Palo
        self.Valor = Valor

    def __str__(self):
        return f"{self.Valor} de {self.Palo}"



for i in range(10):
    palo_aleatorio = random.choice(Palos)
    valor_aleatorio = random.choice(Valores)
    carta = Carta(palo_aleatorio,valor_aleatorio)
    Pila.push(carta)

while Pila.size() > 0 :
    carta_extraida = Pila.pop()
    if carta_extraida.Palo == ("Espada"):
        Pila_Espada.push(carta_extraida)

    if carta_extraida.Palo == ("Basto"):
        Pila_Basto.push(carta_extraida)
    
    if carta_extraida.Palo == ("Oro"):
        Pila_Oro.push(carta_extraida)

    if carta_extraida.Palo == ("Copa"):
        Pila_Copa.push(carta_extraida)

def ordenar_por_valor(Lista):
    Lista.sort(key=lambda carta: carta.Valor)

while Pila_Espada.size() > 0:
    carta_extraida = Pila_Espada.pop()
   # print(carta_extraida)
    Lista.append(carta_extraida)

# Ahora que ya metiste todas las cartas:
ordenar_por_valor(Lista)


while Lista:
    agrega = Lista.pop(0)
    Pila_Ordenada.push(agrega)


#Pila.show()
Pila_Ordenada.show()
#Pila_Espada.show()
#Pila_Basto.show()
#Pila_Oro.show()
#Pila_Copa.show()

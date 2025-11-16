from random import randint
from tda_cola import Cola, arribo, atencion, cola_vacia, barrido

Cola_Nueva = Cola()
Cola_Primos = Cola()  # Cola donde pondremos solo los primos

class Datos_Cola:
    def __init__(self, numeros):
        self.numeros = numeros

    def __str__(self):
        return str(self.numeros)

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def Cargar_Valores():
    Res = int(input("Ingrese cantidad de numeros: "))
    for _ in range(Res):
        Num = randint(1, 100)
        Elem = Datos_Cola(Num)
        arribo(Cola_Nueva, Elem)

def Sacar_Primos():
    aux = Cola()
    while not cola_vacia(Cola_Nueva):
        dato = atencion(Cola_Nueva)
        print("Evaluando:", dato)
        if es_primo(dato.numeros):
            arribo(Cola_Primos, dato)
        arribo(aux, dato)
    
    # Restaurar la cola original
    while not cola_vacia(aux):
        arribo(Cola_Nueva, atencion(aux))

# Programa principal
Cargar_Valores()
print("\n--- Barrido total de la cola ---")
barrido(Cola_Nueva)

print("\n--- Números primos detectados ---")
Sacar_Primos()
barrido(Cola_Primos)

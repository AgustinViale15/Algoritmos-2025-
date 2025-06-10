from Lista import List


class Datos_Lista_1:
    def __init__(self, numeros):
        self.numeros = numeros  # cambiamos a 'caracteres' para que coincida con _str_

    def __str__(self):
        return f"{self.numeros}"

class Datos_Lista_2:
    def __init__(self,numero):
        self.numero = numero

    def __str__(self):
        return f"{self.numero}"

class Datos_Lista_3:
    def __init__(self,numeross):
        self.numeross = numeross

    def __str__(self):
        return f"{self.numeross}"



Valores_1 = [
    Datos_Lista_1(numeros = 1),
    Datos_Lista_1(numeros = 2),
    Datos_Lista_1(numeros = 3),
    Datos_Lista_1(numeros = 4),
    Datos_Lista_1(numeros = 5),
 ]

Valores_2 = [
    Datos_Lista_2(numero = 6),
    Datos_Lista_2(numero = 1),
    Datos_Lista_2(numero = 8),
    Datos_Lista_2(numero = 9),
    Datos_Lista_2(numero = 10),
 ]

Lista_1 = List(Valores_1)
Lista_2 = List(Valores_2)
Lista_3 = List()

def Pasar_datos():
    for i in range(len(Lista_1)):
        Numero =Lista_1[i].numeros 
        Lista_3.append(Numero)
    for i in range(len(Lista_2)):
        Numero =Lista_2[i].numero 
        Lista_3.append(Numero)

def Pasar_datos_no_repetidos():
    elementos_vistos = set()

    # Agregar elementos de Lista_1 sin repetir
    for i in range(len(Lista_1)):
        numero = Lista_1[i].numeros
        if numero not in elementos_vistos:
            Lista_3.append(numero)
            elementos_vistos.add(numero)

    # Agregar elementos de Lista_2 sin repetir
    for i in range(len(Lista_2)):
        numero = Lista_2[i].numero
        if numero not in elementos_vistos:
            Lista_3.append(numero)
            elementos_vistos.add(numero)
    

#Pasar_datos()
Pasar_datos_no_repetidos()
Lista_3.show()
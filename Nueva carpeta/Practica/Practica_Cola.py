from tda_cola import Cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido
from stack import Stack
Nueva_Cola = Cola()
caux = Cola()
Pila = Stack()

class Datos_Cola:
    def init(self,letra):
        self.letra = letra
    def str(self):
        return f"{self.letra}"


def carga_valores():
    Res = int(input("Ingrese cantidad de elementos de la lista: "))
    for i in range(Res):
        Col = input("Ingrese letra: ")
        Elem_de_Cola = Datos_Cola(Col)
        arribo(Nueva_Cola,Elem_de_Cola)

def sacar_Vocales(cola):
    # MUestra el contenido de una cola sin perder datos 
    while (not cola_vacia(cola)):
        dato = atencion(cola)
        print(dato)
        arribo(caux,dato)
        Pila.push(dato)
    while (not cola_vacia(caux)):
        dato = atencion(caux)
        arribo(cola,dato)

def invertir():
    while Pila.size() > 0:
        Sale = Pila.pop()
        arribo(caux,Sale)


carga_valores()
sacar_Vocales(Nueva_Cola)
invertir()
print("Invertido: ")
barrido(caux)
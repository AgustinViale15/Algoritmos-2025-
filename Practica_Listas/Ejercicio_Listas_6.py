from Lista import List

class Numeros:
    def _init_(self, numeros):
        self.numeros = numeros  

    def _str_(self):
        return f"{self.numeros}"
    
Listaa = List()
Lista_Pares = List()
Lista_Impares = List()

Cant = int(input("Ingresar cantidad de numeros a cargar: "))
for i in range(Cant):
    Numero = int(input("Ingrese numero: "))
    Listaa.append(Numero)

for i in range(len(Listaa)):
    if Listaa[i] % 2 == 0:

        Lista_Pares.append(Listaa[i])
    else:
        Lista_Impares.append(Listaa[i])

print("Lista entera: ")
Listaa.show()
print("Lista impares: ")
Lista_Impares.show()
print("Lista pares: ")
Lista_Pares.show()
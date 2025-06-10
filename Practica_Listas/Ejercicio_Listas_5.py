from Lista import List

class Person:
    def __init__(self, caracteres):
        self.caracteres = caracteres  # cambiamos a 'caracteres' para que coincida con _str_

    def __str__(self):
        return f"{self.caracteres}"

Vocales = {"a","e","i","o","u",}
# Creamos una lista vacía personalizada
personas = List()

# Cantidad de caracteres a cargar
A = int(input("Ingresar cantidad de caracteres a cargar: "))

# Carga por teclado
for i in range(A):
    T = input(f"Ingrese caracter {i+1}: ")
    persona = Person(T)
    personas.append(persona)

# Mostramos la lista
print("\nLista de caracteres ingresados:")
personas.show()

i = 0
while i < len(personas):
    if personas[i].caracteres in Vocales:
        personas.pop(i)  # eliminamos el elemento
    else:
        i += 1  # solo avanzamos si no eliminamos (para no saltar elementos)

print("\nLista luego de eliminar las vocales:")
personas.show()
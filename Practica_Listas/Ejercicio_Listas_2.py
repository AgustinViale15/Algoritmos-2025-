from Lista import List
Persona = List([
    {"Nombre": "Agus", "Edad": 23,"Promedio":8},
    {"Nombre": "Tomi", "Edad": 20,"Promedio":7},
    {"Nombre": "Cle", "Edad": 19,"Promedio":8.50},
    {"Nombre": "Clowd", "Edad": 15,"Promedio":9},
])

Persona.add_criterion("Edad", lambda x: x["Edad"])
Persona.add_criterion("Promedio", lambda x: x["Promedio"])

print("Personas ordenadas por promedio:")
Persona.sort_by_criterion("Promedio")
Persona.show()

Nota_a_Buscar = 8.50
indice = Persona.search(Nota_a_Buscar, "Promedio")
print(f"\nAlumno con promedio 8.50 {Nota_a_Buscar} está en el índice: {indice}")

Edad_eliminar = 20
ind = Persona.delete_value(Edad_eliminar,"Edad")
print("\nPersona eliminada:", ind)

print("Lista Actualizada: ")
Persona.show()
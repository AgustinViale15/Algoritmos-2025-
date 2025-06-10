from Lista import List

Persona = List([
   {"Titulo": "Agus", "Autor": "Agus","Anio":2003, "Paginas":100},
    {"Titulo": "Tito", "Autor":"Tito","Anio":2010, "Paginas":150},
    {"Titulo": "Cle", "Autor": "Cle","Anio":2009, "Paginas":156},
    {"Titulo": "Clowd", "Autor": "Clowd","Anio":2014, "Paginas":300},
])

Persona.add_criterion("Anio", lambda x: x["Anio"])
Persona.add_criterion("Paginas", lambda x: x["Paginas"])
Persona.add_criterion("Titulo", lambda x: x["Titulo"])

print("Lista ordenada por titulos: ")
Persona.sort_by_criterion("Titulo")
Persona.show()

Libro_Buscado = 2020
art = Persona.search(Libro_Buscado,"Anio")
print("Libro publicado en 2020: ",art )

Eliminar = 300
Russ = Persona.delete_value(Eliminar,"Paginas")
print("Libor eliminado: ",Russ) #VER

print("Lista final: ")
Persona.show()
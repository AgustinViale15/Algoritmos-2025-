from tree import BinaryTree



arbol_binario_Nombre = BinaryTree()
arbol_completo = BinaryTree()
arbol_binario_Capturada = BinaryTree() 


datos_criaturas = [
        ("Ceto", "-"),
        ("Tifón", "Zeus"),
        ("Equidna", "Argos Panoptes"),
        ("Dino", "-"),
        ("Pefredo", "-"),
        ("Enio", "-"),
        ("Escila", "-"),
        ("Caribdis", "-"),
        ("Euríale", "-"),
        ("Esteno", "-"),
        ("Medusa", "Perseo"),
        ("Ladón", "Heracles"),
        ("Águila del Cáucaso", "-"),
        ("Quimera", "Belerofonte"),
        ("Hidra de Lerna", "Heracles"),
        ("León de Nemea", "Heracles"),
        ("Esfinge", "Edipo"),
        ("Dragón de la Cólquida", "-"),
        ("Cerbero", "-"),
        ("Cerda de Cromión", "Teseo"),
        ("Ortro", "Heracles"),
        ("Toro de Creta", "Teseo"),
        ("Jabalí de Calidón", "Atalanta"),
        ("Carcinos", "-"),
        ("Gerión", "Heracles"),
        ("Cloto", "-"),
        ("Láquesis", "-"),
        ("Átropos", "-"),
        ("Minotauro de Creta", "Teseo"),
        ("Harpías", "-"),
        ("Argos Panoptes", "Hermes"),
        ("Aves del Estínfalo", "-"),
        ("Talos", "Medea"),
        ("Sirenas", "-"),
        ("Pitón", "Apolo"),
        ("Cierva de Cerinea", "-"),
        ("Basilisco", "-"),
        ("Jabalí de Erimanto", "-")
    ]

for criatura, Capturador in datos_criaturas:
    arbol_binario_Nombre.insert(criatura, Capturador)


#A
arbol_binario_Nombre.in_order_Ej_23()



# B
print("")
print("Cargar descripciones de criaturas") 






descripciones_predefinidas = {
    "Ceto": "Diosa primordial del mar, madre de monstruos marinos",
    "Tifón": "Monstruo gigante y poderoso, el más mortífero de la mitología griega",
    "Equidna": "Ninfa monstruosa, mitad mujer hermosa y mitad serpiente",
    "Medusa": "Gorgona con serpientes por cabello que convertía en piedra",
    "Ladón": "Dragón de cien cabezas que guardaba las manzanas de oro del Jardín de las Hespérides",
    "Quimera": "Monstruo que escupía fuego con cabeza de león, cuerpo de cabra y cola de serpiente",
    "Hidra de Lerna": "Serpiente acuática de múltiples cabezas que regeneraba dos por cada una cortada",
    "León de Nemea": "León de piel invulnerable que aterrorizaba la región de Nemea",
    "Esfinge": "Criatura con cuerpo de león, cabeza humana y alas de águila que planteaba acertijos",
    "Cerbero": "Perro de tres cabezas que guardaba la entrada al Inframundo",
    "Cerda de Cromión": "Jabalí gigante y feroz que aterrorizaba la región de Cromión",
    "Ortro": "Perro de dos cabezas, hermano de Cerbero e hijo de Tifón y Equidna",
    "Toro de Creta": "Toro salvaje que sembraba el terror en Creta",
    "Jabalí de Calidón": "Enorme jabalí enviado por Artemisa para castigar a Calidón",
    "Gerión": "Gigante de tres cuerpos que poseía magníficos rebaños de ganado",
    "Minotauro de Creta": "Criatura con cuerpo de hombre y cabeza de toro en el laberinto de Creta",
    "Argos Panoptes": "Gigante de cien ojos que vigilaba constantemente",
    "Talos": "Gigante de bronce que vigilaba Creta, derrotado por Medea",
    "Pitón": "Serpiente gigante que custodiaba el oráculo de Delfos",
    "Sirenas": "Criaturas marinas que con su canto hechizaban a los marineros"
}


for criatura, derrotador in datos_criaturas:
    descripcion = descripciones_predefinidas.get(criatura, "Sin descripción disponible")
    arbol_completo.insert(criatura, {"derrotado_por": derrotador, "descripcion": descripcion})

print("Descripciones cargadas exitosamente")
arbol_completo.in_order()

#C

pos =arbol_completo.search("Talos")
if pos is not None:
    print(" ")
    print(f'Informacion de Talos: {pos.other_values}')

#D
print("")
print("3 héroes o dioses que derrotaron mayor cantidad de criaturas: ")
arbol_binario_Nombre.in_order_derrotas()

#E
print("")
print("Criaturas derrotadas por Heracles") 
arbol_binario_Nombre.in_order_Heracles()

#F
print("")
arbol_binario_Nombre.in_order_no_derrotas()

#G
for criatura, derrotador in datos_criaturas:
    
    info_criatura = {
        "derrotado_por": derrotador,
        "capturada": "-"  
    }
    arbol_binario_Capturada.insert(criatura, info_criatura)

print("")
arbol_binario_Capturada.in_order()


arbol_binario_Nombre.in_order_Ej_23()

#H
Lista = [{"Cerbero","Toro de Creta","Cierva Cerinea","Jabalí de Erimanto"}]
for criatura in Lista[0]:
    pos = arbol_binario_Nombre.search(criatura)
    if pos is not None:
        pos.other_values = "Heracles"

print("")
print("Nueva lista de criaturas capturadas por Heracles: ")
arbol_binario_Nombre.in_order_Ej_23()


#I

print("")
print("Buscar todas las criaturas que contengan Cer en su nombre")
resultados = arbol_binario_Nombre.search_by_partial_match("Cer")

for criatura in resultados:
    
    print(f"Criatura: {criatura.value}")
    criatura.other_values = "Heracles"  

#J
print("")
arbol_binario_Nombre.delete("Basilisco")
arbol_binario_Nombre.delete("Sirenas")
print("Lista sin Basilisco y a las Sirenas:")
arbol_binario_Nombre.in_order_Ej_23()

#K

print("")

resultados = arbol_binario_Nombre.search_by_partial_match("Aves del Estínfalo")

if resultados:
    aves_nodo = resultados[0]  
    
    if hasattr(aves_nodo, 'other_values'):
        if aves_nodo.other_values:
            aves_nodo.other_values = f"{aves_nodo.other_values}. Heracles derrotó a varias"
        else:
            aves_nodo.other_values = "Heracles derrotó a varias"
    else:
        aves_nodo.other_values = "Heracles derrotó a varias"
    
    print(f"Modificado: {aves_nodo.value}")
else:
    print("No se encontraron las Aves del Estínfalo")

arbol_binario_Nombre.in_order_Ej_23()

#L

print("")
print("Modificar Ladón por Dragón Ladón:")
nodo_ladon = arbol_binario_Nombre.search("Ladón")
if nodo_ladon is not None:
    other_value = nodo_ladon.other_values
else:
    other_value = None  

arbol_binario_Nombre.delete("Ladón")
arbol_binario_Nombre.insert("Dragón Ladón", other_value)
arbol_binario_Nombre.in_order_Ej_23()


#M
print("")
arbol_binario_Nombre.listar_por_nivel()

#N
print("")
print("Criaturas capturadas por Heracles")
arbol_binario_Nombre.in_order_Heracles()






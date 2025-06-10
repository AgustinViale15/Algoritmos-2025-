from Lista import List
products = List([
    {"name": "Mouse", "price": 20},
    {"name": "Keyboard", "price": 50},
    {"name": "Monitor", "price": 150},
    {"name": "USB Cable", "price": 10},
])

# Paso 2: registrar criterio de orden por precio
products.add_criterion("price", lambda x: x["price"])

# Paso 3: mostrar productos ordenados por precio
print("Productos ordenados por precio:")
products.sort_by_criterion("price")
products.show()

# Paso 4: buscar producto por precio
precio_a_buscar = 50
indice = products.search(precio_a_buscar, "price")
print(f"\nProducto con precio {precio_a_buscar} está en el índice: {indice}")

# Paso 5: eliminar producto por precio
producto_eliminado = products.delete_value(50, "price")
print("\nProducto eliminado:", producto_eliminado)

# Mostrar lista actualizada
print("\nLista actualizada:")
products.show()
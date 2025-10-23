from heap import HeapMax  
cola_impresion = HeapMax()

#A
cola_impresion.arrive("Empleado 1", 1)
cola_impresion.arrive("Empleado 2", 1)
cola_impresion.arrive("Empleado 3", 1)

#B
print("Primer documento en imprimirse:", cola_impresion.attention())

#C
cola_impresion.arrive("TI 1", 2)
cola_impresion.arrive("TI 2", 2)

#D
cola_impresion.arrive("Gerente 1", 3)

#E
print("Primer documento:", cola_impresion.attention())
print("Segundo documento:", cola_impresion.attention())

#F
cola_impresion.arrive("Empleado 4", 1)
cola_impresion.arrive("Empleado 5", 1)
cola_impresion.arrive("Gerente 2", 3)


#G
print("Documentos restantes:")
while cola_impresion.size() > 0:
    print(cola_impresion.attention())

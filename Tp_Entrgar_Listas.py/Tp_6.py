from Lista import List

class Superheroes:
    def __init__(self, Nombre,Anio,Casa,Bibliografia):
        self.Nombre = Nombre  
        self.Anio = Anio
        self.Casa = Casa
        self.Bibliografia = Bibliografia

    def __str__(self):
        return f"{self.Nombre}-{self.Anio} - {self.Casa}- {self.Bibliografia}"
    
Datos = [
    Superheroes(Nombre = "Linterna Verde",Anio = 1963, Casa = "Marvel",Bibliografia= "traje"),
    Superheroes(Nombre = "Wolverine",Anio = 1934, Casa = "DC",Bibliografia= "Marvel"),
    Superheroes(Nombre = "Dr Strange",Anio = 1945, Casa = "DC",Bibliografia= "traje"),
    Superheroes(Nombre = "Capitana Marvel",Anio = 1965, Casa = "Marvel",Bibliografia= "armadura"),
    Superheroes(Nombre = "Mujer Maravilla",Anio = 1943, Casa = "DC",Bibliografia= "DC)"),
    Superheroes(Nombre = "Flash",Anio = 1986, Casa = "DC",Bibliografia= "DC"),
    Superheroes(Nombre = "Star-Lord",Anio = 1920, Casa = "DC",Bibliografia= "armadura"),
    ]

Lista_Superheroes = List(Datos)

def Eliminar_Linterna_Verde():
    print("")
    Lista_Superheroes.add_criterion("Nombre", lambda x: x.Nombre)
    eliminado = Lista_Superheroes.delete_value("Linterna Verde", "Nombre")
    if eliminado:
        print("Superhéroe eliminado:", eliminado)
    else:
        print("No se encontró a Linterna Verde.")

def Mostrar_Wolverine():
    print("")
    indice = Lista_Superheroes.search("Wolverine","Nombre")
    print("Wolverine aparecio en : ",Lista_Superheroes[indice].Anio)

def Dr_Strange():
    print("")
    indice = Lista_Superheroes.search("Dr Strange", "Nombre")
    Lista_Superheroes[indice].Casa = ("Marvel")
    Lista_Superheroes.show()

def Mostrar ():
    print("")
    print("Superheroes que contienen la palabra “traje” o “armadura” ")
    for i in range (len(Lista_Superheroes)):
        if Lista_Superheroes[i].Bibliografia in (("traje"),("armadura")):
            print(Lista_Superheroes[i].Nombre)

def Anterior():
    print("")
    print("Superheroes antes de 1963")
    for i in range(len(Lista_Superheroes)):
        if Lista_Superheroes[i].Anio < 1963 :
            print(Lista_Superheroes[i].Nombre)
            print(Lista_Superheroes[i].Casa)

def Capitana_Marvel_y_Mujer_Maravilla():
   print("")
   Indice= Lista_Superheroes.search("Capitana Marvel", "Nombre")
   print(Lista_Superheroes[Indice].Casa)
   Indice2= Lista_Superheroes.search("Mujer Maravilla", "Nombre")
   print(Lista_Superheroes[Indice2].Casa)

def Flash_y_StarLord():
   print("")
   Indice= Lista_Superheroes.search("Flash", "Nombre")
   print("Datos Flash ",Lista_Superheroes[Indice])
   Indice2= Lista_Superheroes.search("Star-Lord", "Nombre")
   print("Datos StarLord ",Lista_Superheroes[Indice2])
   
def Anterior():
    print("")
    Letras = ("B","M","S")
    print("Superheroes con la letra B,M,S")
    for i in range(len(Lista_Superheroes)):
        if Lista_Superheroes[i].Nombre[0] in Letras :
            print(Lista_Superheroes[i].Nombre)

def Sumar():
    print("")
    for i in range(len(Lista_Superheroes)):
        if Lista_Superheroes[i].Casa  == ("Marvel") :
            print("Superheroes de marvel: ",Lista_Superheroes[i].Nombre)
        else:
            if Lista_Superheroes[i].Casa  == ("DC") :
                print("Superheroes de DC: ",Lista_Superheroes[i].Nombre)











Eliminar_Linterna_Verde()
Mostrar_Wolverine()
Dr_Strange()
Mostrar()
Anterior()
Capitana_Marvel_y_Mujer_Maravilla()
Flash_y_StarLord()
Anterior()
Sumar()
from Cola import Cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

Cola_Nueva = Cola()
Cola_2 = Cola()
Cola_3 = Cola()
Cola_4 = Cola()

cont = 0
class Datos_Cola:
    def __init__(self, aplicaciones,hora,mensaje):
        self.aplicaciones = aplicaciones
        self.hora = hora
        self.mensaje = mensaje


    def __str__(self):
        return str(self.aplicaciones)
        return str(self.hora)
        return str(self.mensaje)

def hora_a_minutos(hora):
    h, m = map(int, hora.split(":"))
    return h * 60 + m
   
def Cargar_Datos():
    global cont  
    Cant = int(input("Ingresar cantidad de elementos de la cola: "))
    for i in range(Cant):
        Apli = input("Ingrese nombre de la aplicacion: ")
        Hora = input("Ingrese hora de la notificacion (HH:MM): ")
        Mensaj = input("Ingrese mensaje: ")
        Elem = Datos_Cola(Apli, Hora, Mensaj)
        arribo(Cola_Nueva, Elem)
        
        minutos = hora_a_minutos(Hora)
        if hora_a_minutos("11:43") <= minutos <= hora_a_minutos("15:57"):
            arribo(Cola_4, Elem)
            cont += 1  

def Eliminar():
    while not cola_vacia(Cola_Nueva):
        dato = atencion(Cola_Nueva)
        if dato.aplicaciones.lower() != ("facebook"):
            arribo(Cola_2,dato)
        arribo(Cola_3,dato)

def Twitter():
    while not cola_vacia(Cola_3):
     dato = atencion(Cola_3)   
     if dato.aplicaciones.lower() == "twitter" and "python" in dato.mensaje.lower():
         
         print("Aplicacion: ",dato.aplicaciones)
         print("Mensaje: ",dato.mensaje)
    arribo(Cola_Nueva,dato)
    print("Notificaciones de Twitter:")


         

Cargar_Datos()
Eliminar()

print("Cola sin notificaciones de Facebook: ")
barrido(Cola_2)
print("Notificaciones de twitter cuyo mensaje incluya la palabra Python: ")
Twitter()
print("Notidicaciones entre las 11:43 y 15:57: ")
barrido(Cola_4)
print("Cantidad: ",cont)


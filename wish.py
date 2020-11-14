    #Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 13/11/2020 6:00pm 
#Fecha de última Modificación: 13/11/2020 8:00pm
#Versión: 3.8.5
from funciones import GuardarDiccionario,cargarDiccionario,ingresar,actualizar,reporte,eliminar
dic=cargarDiccionario()
def menu():
    """Funcionamiento: muestra el menú y maneja las opciones
    Entradas: N/A
    Salidas: N/A """
    global dic
    while True:
        print("""
                       ▄▄           ▄▄        
▀████▀     █     ▀███▀ ██          ███        
  ▀██     ▄██     ▄█                ██        
   ██▄   ▄███▄   ▄█  ▀███   ▄██▀███ ███████▄  
    ██▄  █▀ ██▄  █▀    ██   ██   ▀▀ ██    ██  
    ▀██ █▀  ▀██ █▀     ██   ▀█████▄ ██    ██  
     ▄██▄    ▄██▄      ██   █▄   ██ ██    ██  
      ██      ██     ▄████▄ ██████▀ ███  ████▄                                     
\n\n""")
        print("1.Ingresar un paquete.\n2.Actualizar estado del paquete.\n3.Eliminar paquete.\n4.Reportar paquete.\n5.Salir")
        opcion=input("Ingrese una opción: ")
        print("")
        if opcion=="1":
            dic=ingresar(dic)
            input("Se ha ingresado el dato, presione enter para continuar.")
        if opcion=="2":
            dic=actualizar(dic)
            input("Se ha realizado el cambio, presione enter para continuar.")
        if opcion=="3":
            dicPrueba=eliminar(dic)
            if type(dicPrueba)==str:
                print(dicPrueba) 
            else:
                dic=dicPrueba
                print('Paquete eliminado')
            input("Presione enter para continuar.")
        if opcion=="4":
            reporte(dic)
            input("datos mostrados satisfactoriamente, presione enter para continuar.")
        if opcion=="5":
            GuardarDiccionario(dic)
            print("Gracias por usar nuestros servicios, hasta pronto.")
            print(dic)
            return ""
        else:
            print("Ingrese un valor valido.")
menu()

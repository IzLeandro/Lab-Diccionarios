from funciones import GuardarDiccionario,cargarDiccionario,ingresar,actualizar,reporte
dic=cargarDiccionario()
def menu():
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
            print()
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
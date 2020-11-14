from funciones import leer,grabar,GuardarDiccionario,cargarDiccionario
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
        if opcion=="1":
            print()
        if opcion=="2":
            print()
        if opcion=="3":
            print()
        if opcion=="4":
            print()
        if opcion=="5":
            GuardarDiccionario(dic)
            print("Gracias por usar nuestros servicios, hasta pronto.")
            return ""
        else:
            print("Ingrese un valor valido.")
menu()
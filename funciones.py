#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 13/11/2020 6:00pm 
#Fecha de última Modificación: 13/11/2020 9:41pm
#Versión: 3.8.5
from archivos import grabar,leer
import re
def GuardarDiccionario(dic):
    """Funcionamiento: pregunta el nombre y llama una funcion que cree el archivo.
    Entradas: dic
    Salidas: N/A """
    pregunta=input("Ingrese el nombre con el que desea guardar el archivo: ")
    grabar(pregunta,dic)
    return ""

def cargarDiccionario():
    """Funcionamiento: Comprueba que los datos ingresados sean correctos y carga el diccionario desde un archivo
    Entradas: N/A
    Salidas: diccionario """
    while True:
        pregunta=input("¿desea cargar un archivo previo? (Si/No): ")
        if pregunta.upper()=="SI":
            pregunta=input("Ingrese el nombre del archivo a cargar: ")
            dic=leer(pregunta)
            print("Datos extraidos desde el archivo correctamente.")
            return dic
        elif pregunta.upper()=="NO":
            return {}
        else:
            print("Ingrese un valor correcto.")
#! FALTA COMPARAR NUMERO DE TELEFONO CONTRA REGEX
def ingresar(dic):
    """Funcionamiento: valida y añade datos al diccionario
    Entradas: dic
    Salidas: dic """
    while True:
        codigo=revisarUltimoCodigo(dic) + 1
        estado=["Por entregar","Entregado","Devuelto"]
        numTelefono=input("digite el número de teléfono: ")
        if not re.match("^\d{8}$",numTelefono):
            print("Ingrese un numero de telefono correcto.")
            continue
        sucursal=input("Digite la sucursal: ")
        preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
        if not re.match("^\d{1,}$", preguntaEstado):
            print("Ingrese solo números.")
            preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
            while not re.match("^\d{1,}$",preguntaEstado):
                print("Ingrese solo números.")
                preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
        preguntaEstado=int(preguntaEstado)
        while preguntaEstado <= 0 or preguntaEstado > 3:
            print("Ingrese solo números.")
            preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
            if not re.match("^\d{1,}$", preguntaEstado):
                print("Ingrese solo números.")
                preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
            while not re.match("^\d{1,}$", preguntaEstado):
                print("Ingrese solo números.")
                preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
            preguntaEstado=int(preguntaEstado)
        if preguntaEstado==1:
            dic[codigo]=[numTelefono,sucursal,10,estado[preguntaEstado-1]]
        else:
            dic[codigo]=[numTelefono,sucursal,0,estado[preguntaEstado-1]]
        return dic

def revisarUltimoCodigo(dic):
    """Funcionamiento: retorna la ultima llave utilizada.
    Entradas: dic
    Salidas: int """
    ultimo=0
    for i in dic.keys():
        ultimo=i
    return ultimo

def actualizar(dic):
    """Funcionamiento: cambia el estado del paquete a uno de los 3 disponibles, de ser necesario, modifica los dias restantes
    Entradas: dic
    Salidas: dic """
    while True:
        try: codigoABuscar=eval(input("digite el código del paquete: "))
        except:
            print("Solo se admiten números.")
        for i in dic.keys():
            if i == codigoABuscar:
                preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
                try:
                    preguntaEstado=eval(preguntaEstado)
                    if preguntaEstado <=0 or preguntaEstado > 3:
                        print("Ingrese un valor entre 1 y 3.")
                        continue
                except:
                    print("Ingrese solo números.")
                    continue
                if preguntaEstado==1:
                    dic[i][2]=5
                else:
                    dic[i][2]=0
                return dic
        else:
            print("El código indicado no se encuentra en el registro.")

def reporte(dic):
    """Funcionamiento: imprime la información contenida en el diccionario
    Entradas: dic
    Salidas: dic """
    print("Total de paquetes registrados: ",revisarUltimoCodigo(dic))
    for i in dic.keys():
        print("Numero de paquete:",i)
        print("Numero de Telefono:",dic[i][0])
        print("Sucursal:",dic[i][1])
        print("Cantidad de días hábiles:",dic[i][2])
        print("Estado:",dic[i][3],"\n")   
    return dic

def eliminar(dic):
    """Funcionamiento: elimina un paquete seleccionado por el usuario
    Entradas: dic
    Salidas: dic o mensaje """
    numPaquete=input('Digite el número del paquete a eliminar. Recuerde que este no es su número de telefono: ')
    while not re.match("^\d{1,}$",numPaquete):
        print('Lo que se ingresó no es válido')
        numPaquete=input('Digite el número del paquete a eliminar. Recuerde que este no es su número de telefono: ')
    for key in dic:
        if int(numPaquete)==key:
            eleccion=input('¿Está seguro que quiere borrarlo?: ')
            if eleccion.upper()=='SI':
                del dic[key]
                return dic
            if eleccion.upper()=='NO':
                return 'Volviendo al menú...'
            while eleccion.upper()!='NO' or eleccion.upper()!='SI':
                print('Opción no válida')
                eleccion=input('¿Está seguro que quiere borrarlo?: ')
                if eleccion.upper()=='SI':
                    del dic[key]
                    return dic
                if eleccion.upper()=='NO':  
                    return 'Volviendo al menú...'
    return 'No se encuentra registrado el número que se indica'

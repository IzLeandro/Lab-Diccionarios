from archivos import grabar,leer
import re
def GuardarDiccionario(dic):
    pregunta=input("Ingrese el nombre con el que desea guardar el archivo: ")
    grabar(pregunta,dic)
    return ""

def cargarDiccionario():
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
    while True:
        codigo=revisarUltimoCodigo(dic) + 1
        estado=["Por entregar","Entregado","Devuelto"]
        numTelefono=input("digite el número de teléfono: ")
        if not re.match("^\d{8}$",numTelefono):
            print("Ingrese un numero de telefono correcto.")
            continue
        sucursal=input("Digite la sucursal: ")
        preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
        try:
            preguntaEstado=eval(preguntaEstado)
            if preguntaEstado < 0 and preguntaEstado > 4:
                print("Ingrese un valor entre 1 y 3.")
                continue
        except:
            print("Ingrese solo números.")
            continue
        if preguntaEstado==1:
            dic[codigo]=[numTelefono,sucursal,10,estado[preguntaEstado-1]]
        else:
            dic[codigo]=[numTelefono,sucursal,0,estado[preguntaEstado-1]]
        return dic

def revisarUltimoCodigo(dic):
    ultimo=0
    for i in dic.keys():
        ultimo=i
    return ultimo

def actualizar(dic):
    while True:
        try: codigoABuscar=eval(input("digite el código del paquete: "))
        except:
            print("Solo se admiten números.")
        for i in dic.keys():
            if i == codigoABuscar:
                preguntaEstado=input("1.Por entregar.\n2.Entregado.\n3.Devuelto.\nCual es el estado del paquete?: ")
                try:
                    preguntaEstado=eval(preguntaEstado)
                    if preguntaEstado < 0 and preguntaEstado > 4:
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
    print("Total de paquetes registrados: ",revisarUltimoCodigo(dic))
    for i in dic.keys():
        print("Numero de paquete:",i)
        print("Numero de Telefono:",dic[i][0])
        print("Sucursal:",dic[i][1])
        print("Cantidad de días hábiles:",dic[i][2])
        print("Estado:",dic[i][3],"\n")   
    return dic
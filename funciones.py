from archivos import grabar,leer

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
        numero=input("digite el número de teléfono: ")
        sucursal=input("Dijite la sucursal: ")
        
        return dic

def revisarUltimoCodigo(dic):
    ultimo=0
    for i in dic.keys():
        ultimo=i
    return ultimo

dic={1:"a",2:"b",3:"c"}


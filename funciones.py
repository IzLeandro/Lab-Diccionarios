import pickle

def grabar(nomArchGrabar,lista):
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
        print("Archivo guardado.")
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def leer(nomArchLeer):
    dic={}
    try:
        f=open(nomArchLeer,"rb")
        dic = pickle.load(f)
        f.close()
    except:
        print("El archivo indicado no existe, ingrese un nombre correcto.")
    return dic

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

def ingresar(dic):
    while True:
        return dic

def revisarUltimoCodigo(dic):
    ultimo=0
    for i in dic.keys():
        ultimo=i
    return ultimo

dic={1:"a",2:"b",3:"c",4:"d"}
print(revisarUltimoCodigo(dic))
#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 13/11/2020 6:00pm 
#Fecha de última Modificación: 13/11/2020 8:00pm
#Versión: 3.8.5
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
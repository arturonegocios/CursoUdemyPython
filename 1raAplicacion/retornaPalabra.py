import json
import difflib
from numpy.core.defchararray import upper

data = json.load(open("data.json"))

def palabra (entrada):
    return data[entrada]

def chequeador(entrada):
    if len(difflib.get_close_matches(entrada,data.keys())) > 0:
        return difflib.get_close_matches(entrada,data.keys())[0]
    else:
        return "La palabra no existe"

def output(entrada):
    output = palabra(entrada)
    for item in output:
        print(item)

while True:
    entrada = input("Entre Una Palabra en Ingles: ")
    chequeo = chequeador(entrada)
         
    if entrada.lower() in data:
        output(entrada.lower())
    elif entrada.capitalize() in data:
        output(entrada.capitalize())
    elif entrada.upper() in data:
        output(entrada.upper())
    
    elif chequeo in data:
        yn = input(" Quizas la palabra es %s presione Y  para continuar o N para evauluar otra palabra " % chequeo)
        if yn == "Y" or yn=="y":
            output(chequeo)
        elif yn == "N" or yn=="n":
            print('La palabra no existe')
        else:
            print("Introduzca Y o N ")
    else:
        print('La palabra no existe')
        



archivo = "archivoModelo.txt"

lista =[]
dictNodos={}

def guarda_nodos(archivo):
    with open(archivo) as objecto:
        n=0
        for line in objecto:
            if line.rstrip().startswith("NODE"):
                n+=1
                dictNodos.__setitem__(str("NODO"+"_"+str(n)), line.rsplit()) 
               


guarda_nodos(archivo)
print(dictNodos)
import mysql.connector
import difflib

#crear variable para conectarte a la base de datos
results = []

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

def palabraMascercana(entrada, results):    #Me busca la palabra mas cercana
    if len(difflib.get_close_matches(entrada,results))>0:
        return difflib.get_close_matches(entrada,results)[0]
    else:
        return "Palabra no existe"

def listaChequeo(output): #me crea una lista para buscar palabras, no guarda las definiciones 
    results=[]
    for item in output:
        results.append(item[0])
    return results

def navegaLista(entrada,output): #crea una lista de salida solo con las definiciones de acuardo la palabra que introduci.
    salida = []
    for item in output:
        if item[0]==entrada or item[0]==entrada.upper() or item[0] == entrada.capitalize():
            salida.append(item[1])
        else:
            continue
    return salida


entrada =  input("Entre una palabra en ingles: ")
#creo un cursor para navergar  la base de datos
cursor  =  con.cursor()
query = cursor.execute("SELECT *FROM Dictionary WHERE Expression LIKE '%s"%entrada[0] + entrada[1]+"%'")
output = cursor.fetchall()
results =  listaChequeo(output) # con el output me guarda una lista de posibles palabras
palabra = palabraMascercana(entrada,results)
entrega = navegaLista(entrada,output) #Introdujo la palabra bien


if entrada.lower() in results:
    for item in entrega:
        print(item)
elif entrada.upper() in results:
    for item in entrega:
        print(item)
elif entrada.capitalize() in results:
    for item in entrega:
        print(item)


#buscar en la lista resulst la palabra mas cercana

elif palabra or palabra.upper() or palabra.capitalize() in results:
    entrega = navegaLista(palabra,output)
    while True:
        YN = input("La palabra introducida es incorrecta, usted se refiere a %s? Y/N "%palabra)
    
        if YN == "y" or YN == "Y":
            for item in entrega:
                print(item)
            break
        elif YN == "n" or YN == "N":
            print("Palabra no existe")
            break
        else:
            print("Introdusca Y/N")
            continue

else:
    print("Palabra no existe")
        



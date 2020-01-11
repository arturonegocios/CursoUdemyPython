import mysql.connector
import json

#nos conectamos con la base de datos
con = mysql.connector.connect(
    user = "arturo",
    password= "arturo",
    host = "localhost",
    database = "newdatabase"
)
tabla = "temperatures"
TablaC1 = "Date"
TablaC2 = "Source"
TablaC3 = "Temperature"
ValorC1 = ""
ValorC2 = ""
ValorC3 = ""
Columnas = "("+ TablaC1 +"," +TablaC2 + "," + TablaC3 +")"
sql = "INSERT INTO "
sql2 ="VALUES "
#creo el cursor para navegar la base de datos
cursor =  con.cursor()

# print((sql+tabla+" "+str(Columnas)+" " +str(Values)+"'"))


#cargamos el json to una lista usando load de la libreria json(y open de python(Nombre y ubicacio del archivo))

data = json.load(open("monthly_json.json"))

#el json es una lista compuesta de diccionarios los keys son "Date","Mean" y "Source" que corresponde a su entrada en la tabla de la base de datos
#el obejectivo es leer la lista, cargar el diccionario y identificar el correspondiente key y almacenarolo en la correspodiente columna en la tabla temperatura



for item in data:
    if item['Date'] and item['Mean'] and item['Source']:
        ValorC1 = item['Date']
        ValorC2 = item['Source']
        ValorC3 = item['Mean']
        Values = (ValorC1,ValorC2,ValorC3)
        cursor.execute(sql+tabla+" "+str(Columnas)+" "+ sql2 +str(Values))
        print(sql+tabla+" "+str(Columnas)+" "+ sql2 +str(Values))
        print("ejecutando")

    else:
        print("Error leyendo el Json")


con.commit()



        

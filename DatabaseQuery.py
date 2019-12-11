import mysql.connector
import difflib

#crear variable para conectarte a la base de datos

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

output =[]

def chequeo(entrada,output):
    if len(difflib.get_close_matches(entrada,output))>0:
        return (difflib.get_close_matches(entrada, output)[0])
    else:
        print("algo mal")

def palabra(entrada):

    if entrada.lower()== result[0]:
        return result
    elif entrada.capitalize()== result[0]:
        return result
    elif entrada.upper()== result[0]:
        return result
    else:
        return result

    

entrada = input("Entre Una Palabra en ingles: ")
cursor = con.cursor()
retorno =  palabra(entrada)
querysimilar = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s"%retorno[0] + retorno[1] + "%'")
buscarsimilar = cursor.fetchall()

for item in buscarsimilar:
    output.append(item[0])

salida = str(chequeo(entrada,output))
print(salida)

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE '%s"%salida+"%'")
result = cursor.fetchall()

print(result[0])

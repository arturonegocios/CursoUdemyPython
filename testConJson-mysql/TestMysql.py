import mysql.connector
import json

#prueba de coneccion

con = mysql.connector.connect(
    user = "arturo",
    password = "arturo",
    host = "localhost",
    database = "newdatabase"
)

#test jason

data =  json.load(open("monthly_json.json"))
print(data)
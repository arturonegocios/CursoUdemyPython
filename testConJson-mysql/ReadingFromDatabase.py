import datetime
import mysql.connector

con =  mysql.connector.connect(
    user ="arturo",
    password = "arturo",
    host = "localhost",
    database = "newdatabase"

)

print(con._password)
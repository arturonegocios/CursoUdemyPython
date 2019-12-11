def tempMeasurament(mytemp):
    if mytemp > 7:
        return "Warm"
    else:
        return "Cold"
print(tempMeasurament(5)) #El valor no puede ser introducido por el usuario

# user_input = input("Entre la Temperatura: ") dara un error porque hay que convertir string a valor numerico float int double

user_input = float(input("Entre la Temperatura:"))
print("Esta haciendo:", tempMeasurament(user_input))

#string formating in python

user_input = input("Entre su nombre:")
message = "Hello %s" %user_input #metodo usado en toda las versiones de python 
message2 = f"Hello {user_input}" #metodo usado en python 3.6 en adelante

print(message)
print(message2)

#multiple entradas
nombre = input("Entre su nombre:")
apellido = input("Entre su apellido:")
Cuando = "Hoy"

message = "Hello %s %s" % (nombre, apellido) #metodo usado en toda las versiones de python. Para entra multiple variables usar %s x numero de variables y (varz,var2,.......) 
message2 = f"Hello {nombre} {apellido}, 'que pasa' {Cuando} " #metodo usado en python 3.6 en adelante " {variable} espacio {variable}, mas argumentos espacio {mas variables} 

print(message)
print(message2)

#ejercicio
def greeting(name):
    return "Hi %s" %name.title()
print(greeting("marry"))
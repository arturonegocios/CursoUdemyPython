#chequea la entrada del usuario
#uso de while loop en interfaz de usuario

usuario = ""

while usuario != "Arturo":
    usuario = input("Entre el usuario: ")

#while loop con break y continue

while True:
    usuario = input("Entre el usuario2: ")
    if usuario == "Arturo":
        break
    else:
        continue
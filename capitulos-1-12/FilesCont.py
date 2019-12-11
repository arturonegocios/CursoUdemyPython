with open("data.txt", "r") as myfile:
    contenido = myfile.read()

with open("data.txt", "a+") as myfile:
    myfile.write(contenido)
    myfile.write(contenido)
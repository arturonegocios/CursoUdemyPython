# myfile = open("frutas.txt")
# content = myfile.read() # salva el contenido de un archivo en una variable
# myfile.close() #cierra el archivo
# print(content)

# my_file = open("frutas.txt")
# contenido = my_file.read()
# print(contenido[:91])

def conteoChar(caracter, filepath):
    with open(filepath) as myfile: #mejor forma de abrir un archivo ya que los cierra automaticamente
        contenido = myfile.read()
        return contenido.count(caracter)


print(conteoChar('a','frutas.txt'))


with open("vegetales/vegetales.txt","w") as myfile:
    myfile.write("Tomate\n")
    myfile.write("Lechuga\n")
    myfile.write("espinacas\n")
    myfile.write("AJO\n")

with open("frutas.txt", 'r') as myfile:
    contenido =  myfile.read()

with open("vegetales/first.txt", 'w') as myfile:
    myfile.write(contenido[:12])


with open("frutas.txt", 'a+') as myfile:  #'r' lee 'w' escribe 'a' anade 'a+' anade una linea 
    myfile.write("\nChinolas")
    myfile.seek(0)# mueve el cursor a la posicion indicada
    contenido = myfile.read()

print(contenido)

with open("bear1.txt", "r") as myfile:
    contenido = myfile.read()

with open("bear2.txt", "a+") as myfile:
    myfile.write(contenido)
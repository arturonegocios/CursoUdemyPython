monday_temperatures = [18.9, 25.4, 18.5]

for temperature in monday_temperatures:
    print(round(temperature))

for letra in 'hello':
    print(letra.title())

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

for color in colors:
    if color > 50:
        print(color)

colors2 = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors2:
    if type(color) == int:
        print(color)


print("")

for color in colors2:
    if type(color)==int and color>50:
        print(color)

#iteraccion en diccionarios

notas_estudiantes = {"Jose": 89, "Carla": 75, "Adrian": 80}

for nota in notas_estudiantes.items(): #interactua devolviendo items y su valor en una tupla
    print(nota)
print("")

for nota in notas_estudiantes.keys(): #interactua sombre los items
    print(nota)
print("")

for nota in notas_estudiantes.values(): #interactua sombre los valores
    print(nota)
print("")

#formato de texto con for loop
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
    
for pair in phone_numbers.items():
    print("{} tiene el numero {}".format(pair[0], pair[1]) )
print("")
#formato de texto con for loop otro metodo

for key, value in phone_numbers.items():
    print("{} tiene el numero{}".format(key, value))
print("")

#ejercicio
for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))
print("")
p = "+"
p.replace('+', '00',1)
print(p)

#ejercicio
for number in phone_numbers.values():
    print(number.replace("+", "00"))
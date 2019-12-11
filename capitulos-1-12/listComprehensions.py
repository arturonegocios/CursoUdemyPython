temps = [240,230,210]

new_temps = [temp / 10 for temp in temps ] #almacena en temp el contenido del repectivo indece de temps y lo divide en 10  para almacenarlo en la lista new_temps
print(new_temps)

temps2 = [240,320,-9999, 310,280]

new_temps2 = [temp / 10 for temp in temps2 if temp !=-9999]
print(new_temps2)

lista = [99,"no data", 10, 15, "no data"]

def returnNumbers(my_list):
    return [number for number in my_list if number !='no data'] #built in functions no funcionan dentro de comprehesions list



print(returnNumbers(lista))

def greaterThanZero(my_list):
    return [number for number in my_list if number > 0]

print(greaterThanZero([10,-99,8,-96]))

lista3 = [temp / 10 if temp !=-9999 else 0 for temp in temps2] # el for loop va al final is hay un else  
print(lista3)

def zeroInstead(my_list):
    return[number if number !="no data" else 0 for number in lista]

print(zeroInstead(lista))

listaStrings = ["1.2", "1.5", "1.7"]

def stringToNumbers(my_list):
    lista= [float(number) for number in my_list]
    return sum(lista)

print(stringToNumbers(listaStrings))
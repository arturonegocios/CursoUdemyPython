monday_temperatures = [18.9, 25.4, 18.5]
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445

monday_temperatures.append(20.5) #metodo para anadir datos a una lista
seconds.append(current)
print(seconds)
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)
print(seconds)
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)
seconds.remove(1.023458894)
seconds.remove(1.10001399445)
print(seconds)
print(monday_temperatures[2])# los brackets me permiten ver el valor de un indice
print(monday_temperatures)
print(monday_temperatures.index(25.4))  #metodo  devuelve la posicion de un valor en la lista
monday_temperatures.clear() #borra los valores de la lista
print(monday_temperatures)
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])
print(serials[0], serials[2], serials[5])
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

#acceder por slice(cortar) a la lista

print(workdays[0:3]) #del 1-4
print(workdays[3:4]) #del 4-5
print(workdays[:4]) #del inicio de la lista al 5
print(workdays[1:]) #del 2 al final de la lista

#usar indeces negativos para contasr de atras a adelante en una lista

print(workdays[-1]) #me da el valor del ultimo index
print (workdays[-2:])# del antepenultimo al ultimo
print (workdays[:-2])# del antepenultimo al primero

#Indices en strings y slicings
palabra = "Hola"
print(palabra[3])
print(palabra[:3])
print(palabra[2:6])
#chain slice de lista conteniendo strings
print(workdays[1][0])# [] la posicion del string y [] los caracteres que quiero ver su valor
print(workdays[1][0:2])# [] la posicion del string y [] los caracteres que quiero ver su valor
alfa =['abc' , 'def', 'ghi', 'jkl', 'mno']
print(alfa[-2][-2])
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])
print(letters[-4:])

#indices en diccionarios

#traductor
ing_spanish = {"Calle": "Road", "Sol": "Sun", "Mesa": "Table", "Escritorio": "Desk"} #para acceder al valor de un diccionario introducimos en los brackets la entrada y nos devuelve su valor
print(ing_spanish["Sol"])
print(ing_spanish["Escritorio"])

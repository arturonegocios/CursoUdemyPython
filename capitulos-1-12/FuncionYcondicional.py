#CONDICIONALES  
#funcion que identifica si la es una lista o un diccionario

monday_temperatures = [18.9, 25.4, 18.5]
Students_Grades = {"maria": 45,"jose": 50,"carla": 70}

def mymean(value):
    if type(value)== dict: #type me devuelve el tipo de variable que esto usando
        mean = sum(value.values())/len(value) #values() builtin metodo para obteners los valores de un diccionario
    else:
        mean = sum(value)/len(value)
    return mean

print("lista", mymean(monday_temperatures))
print("diccionario", mymean(Students_Grades))

j = "password"
def passw(mypass):
    if mypass.__len__() > 8:
        return True
    else:
        return False
print (passw(j))

def tempMeasurament(mytemp):
    if mytemp > 7:
        return "Warm"
    else:
        return "Cold"
print(tempMeasurament(5))

#elif para multiples condicionales
x = 4
y = 1

if x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual a y") 
else:
    print("x es menor que y")

def tempMeasurament2(mytemp):
    if mytemp > 25:
        return "Hot"
    elif mytemp >= 15 and mytemp <= 25:
        return "Warm"
    else:
        return "Cold"

print(tempMeasurament2(15))
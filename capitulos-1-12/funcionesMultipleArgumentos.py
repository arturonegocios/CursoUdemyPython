
def area (a, b):
    return a * b

print(area(4, 5)) 

def area2 (a, b=7): #non keyword [parameters]
    return a * b


print(area2(3))

def mean(*args): #* dice qur podemos introducir una indefinida cantidad de nunmeros esta funcion retorna una tupla con indefinida entradas
    return sum(args) / len(args)

print(mean(4,5,4,6,9))



def UpperList(*args):
    
  lista = [x.upper() for x in args ]
  return sorted(lista)
  

print(UpperList("alacier", "bnow", "cceberg"))

def number(**kewargs): # define una funcion con ilimitado keyword arguments retorna un diccionario con indefinidas entradas
    return kewargs

print(number(a=5, b= 10, c= 8))
mylista = [1,10,25,35]
mydim = 8
onzas = 45.5

def mean(mylist): #def se usar para definir una funcion en python
    
    mymean = sum(mylist)/len(mylist)
    return mymean


print(mean(mylista))

def lengther(lst):
    mylengther = len(lst)
    return mylengther

print(lengther(mylista))

def areaCalc(dim):
    area = dim * dim
    return area

print(areaCalc(mydim))

def ouncesToMillis(myOunces):
    millis = myOunces * 29.57353
    return millis

print(ouncesToMillis(onzas))



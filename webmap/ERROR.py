def divide(a,b):
    try:
       return a/b
    except: 
        return 'Division por zero'

print(divide(1,0))
c = 1

if c == 1:
    print("yes")
else:
    print("no")

if c == 1 and c==1:
    print("yes")
else:
    print("no")

if c == 1 or c==-1:
    print("yes")
else:
    print("no")


def foo(x, myArray):
    if x in myArray:
        return True
    else:
        return False

print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))
x=10
if isinstance(x,int) or isinstance (x, float) or x==1: #isinstance es una builtin metodo para determinal el tipo de variable
    print("is valid")


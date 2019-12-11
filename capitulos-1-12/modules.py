import time #importa el module time el cual es un modulo builtin python en c
import os # modulo hecho en python
import pandas #importando un libreria externa


# while True:
#     if os.path.exists("frutas.txt"):
#         with open("frutas.txt", "r") as myfile:
#             print(myfile.read())
#     else:
#         print("Archivo no existe")
#     time.sleep(3)

while True:
    if os.path.exists("temps-today.csv"):
        data = pandas.read_csv("temps-today.csv")
        print(data.mean()["st1"])
    else:
        print("Archivo no existe")
    time.sleep(3)
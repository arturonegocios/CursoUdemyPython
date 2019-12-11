listaEntrada = []
Pregunta = ("que","cuando" ,"donde","porque","hacia","como")
Texto = ""


def creador_de_sentencias(frase):
    capitalized =  frase.capitalize()
    if frase.startswith(Pregunta):
        return "{}? ".format(capitalized)
    else:
        return "{}. ".format(capitalized)

# while True:
#     fraseEntrada = input("Por favor diga algo: ")
    
#     if fraseEntrada == "/end":
#         print(Texto)
#         break
#     else:
#         Texto += " "+ creador_de_sentencias(fraseEntrada)
#         continue



while True:
    fraseEntrada = input("Por favor diga algo: ")
    
    if fraseEntrada == "/end":
        break
    else:
        listaEntrada.append(creador_de_sentencias(fraseEntrada)) 
        continue


print(Texto.join(listaEntrada))
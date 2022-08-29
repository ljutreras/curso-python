lista_nombres = ["Paco", "Emilio", "Javier"]

for nombre in lista_nombres:
    print(nombre)
else:
    print("Ciclo terminado") #Se ejecuta cuando todo se recorre sin interrupciones

""" 
Paco
Emilio
Javier
Ciclo terminado """


for nombre in lista_nombres:
    print(nombre)
    if nombre == "Emilio":
        break
else:
    print("Ciclo terminado") #No se ejecuta, se interrumpio el ciclo
""" 
Paco
Emilio 
"""
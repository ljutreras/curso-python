nombres = ["Paco", "Emilio", "Javier"]

""" al encontrar el elemento descrito en la sentencia IF, detenemos la iteracion el ciclo """
for elemento in nombres:
    if elemento == "Emilio":
        break
    print(elemento)

""" Al encontrar el elemento descrito en la sentencia IF, saltamos el elemento y continuamos la iteracion """
for elemento in nombres:
    if elemento == "Emilio":
        continue
    print(elemento)

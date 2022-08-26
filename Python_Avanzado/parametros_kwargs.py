def funcion_kwargs(**kwargs): # **kwargs nos genera un diccionario
    print(kwargs)
    for llave,valor in kwargs.items():
        print(f"Llave: {llave}, valor: {valor}")

funcion_kwargs(nombre="Leonardo") #De esta manera creamos la llave "Nombre" junto al valor "Leonardo"
def validar_x(x):
    if x < 1:
        raise Exception("La variable x debe ser mayor a 1") #Levantamos una excepcion con un mensaje personalizado
    else:
        print("x es mayor a 1")

""" x = 0.3 """
x = 2
validar_x(x)
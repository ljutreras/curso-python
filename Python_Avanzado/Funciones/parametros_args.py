""" def calcular_perimetro(lado1,lado2,lado3,lado4):
    perimetro = lado1+lado2+lado3+lado4
    return perimetro """

def calcular_perimetro(*args):  #*args genera una tupla
    perimetro = 0               #Inicializamos la variable en 0
    for lado in args:           #Recorremos con la variable lado el parametro *args
        perimetro += lado       #A la variable inicializada le agregamos el valor recorrido en *args
    return perimetro            #Retornamos el perimetro

perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)

triangulo = calcular_perimetro(1,2,3)
print(triangulo)

#De esta manera generamos una funcion con parametros sin limite, esto gracias a *args
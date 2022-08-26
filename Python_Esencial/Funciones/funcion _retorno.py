""" def perimetro_cuadrado(lado):
    perimetro = lado*4
    return perimetro

def area_cuadrado(lado):
    area = lado * lado
    return area

perimetro = perimetro_cuadrado(5)
area = area_cuadrado(5) """

def calcular_cuadrado(lado):
    perimetro = lado*4
    area = lado * lado
    return area, perimetro

area, perimetro = calcular_cuadrado(5)

print(f"Area: {area}, Perimetro: {perimetro}")
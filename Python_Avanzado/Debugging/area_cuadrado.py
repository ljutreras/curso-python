def calcular_area_cuadrado(lado):
    """ Calcular el area de un cuadrado al recibir la longitud del lado """
    area = lado * lado
    return area

lado_cuadrados = [1,3,4]
area_cuadrado = []
for lado in lado_cuadrados:
    area = calcular_area_cuadrado(lado)
    area_cuadrado.append(area)

#python3 -m pdb area_cuadrado.py 

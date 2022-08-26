# from cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.cuadrado import area_cuadrado, perimetro_cuadrado #Importamos desde una carpeta un paquete y modulo especifico
from figuras.circulo import area_circulo, perimetro_circulo

""" lado = 5
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado) """

lado = 4
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado)

radio = 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)

}

print(circulo)

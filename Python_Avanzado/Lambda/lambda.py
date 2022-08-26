#Lambda Argumentos: Expresion

multiplicacion = lambda num: num*2 #num representa el parametro, luego asignamos la funcion a realizar, en este caso num*2
print(multiplicacion(2)) #mediante la variable le damos los argumentos de num, en este caso 2
# Por lo que imprime el resultado de 2*2

#Esta funcion no se puede convertir a Lambda por la complejidad de su funcion
#Debido a que contiene Ciclos y condicionales
""" def separar_par_impar(lista_numeros):
    pares =[]
    impares = []
    for numero in lista_numeros:
        if numero%2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
 """

 #Esta funcion se puede convertir a Lambda, debido a la sencillez de su funcion
def calcular_area_cuadrado(lado):
    return lado ** 2

#Esta linea de codigo representa la funcion anterior en solo una linea
calcular_cuadrado = lambda lado: lado ** 2

#imprimimos la variable junto a la funcion Lambda, y le asignamos un argumento
print(calcular_cuadrado(2))
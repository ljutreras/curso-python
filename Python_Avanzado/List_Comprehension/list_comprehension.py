"""  
lista = [expresion(elemento) for elemento in objeto_iterable]
"""

def calcular_cuadrado(numero):
    return numero**2

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)

#Colocamos la expresion directamente (num**2) creamos la iteracion (for num in) agregamos la lista a iterar (lista_num)
lista_comprehension = [num**2 for num in lista_num]
print("List comprehension", lista_comprehension)

#Colocamos la funcion (calcular_cuadrado(num)) creamos la iteracion (for num in) agregamos la lista a iterar (lista_num)
lista_comprehension2 = [calcular_cuadrado(num) for num in lista_num]
print("Lista2", lista_comprehension2)
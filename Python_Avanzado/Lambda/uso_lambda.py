lista_numeros = [1,2,3,4,5,6,7,8]

""" Filtramos la lista numeros y la llevamos a la expresion, por cada numero que pase la expresion
se enviará a la lista_pares en forma de lista """

lista_pares = list(filter(lambda num : num % 2 == 0, lista_numeros))
print(lista_pares) #Imprimimos la lista_pares y nos da el resultado [2,4,6,8]


nueva_lista = list(map(lambda numero : numero * 10, lista_numeros))
print(nueva_lista)

#Las funciones lambda NO son recomendadas por la comunidad, es por ello que se recomienda no abusar de ello
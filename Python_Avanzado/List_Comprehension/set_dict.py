lista_num = [1,2,2,2,4,5,6,8,8,9,10]

#De esta manera creamos una lista sin numeros repetidos
#Representamos el metodo set con unas llaves {list_comprehension}
set_pares = {num for num in lista_num if num % 2 == 0}
print(set_pares) #{2, 4, 6, 8, 10}

vocales = "aeiou"

#LOWER Minusculas 
#UPPER Mayusculas
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)
"""
    {
    'a': 'A', 
    'e': 'E', 
    'i': 'I', 
    'o': 'O', 
    'u': 'U'
    }
"""
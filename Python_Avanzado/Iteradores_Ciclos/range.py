""" 
range(inicio, fin, paso)
"""

serie1 = range(5) #Rango del 0 al 5 sin contabilizar el 5
print(list(serie1)) #[0, 1, 2, 3, 4]

serie2 = range(5,10) #Rango del 5 al 10 sin contabilizar el 10
print(list(serie2)) #[5, 6, 7, 8, 9]

serie3 = range(5,10,2) #Rango del 5 al 10 saltando de 2 en 2
print(list(serie3)) #[5, 7, 9]
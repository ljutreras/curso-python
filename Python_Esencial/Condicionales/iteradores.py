lenguajes = ["Python", "Java", "Go"]

""" for index in range(len(lenguajes)):
    print("indice", index)
    print("elemento", lenguajes[index]) """

""" i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i+=1 """

diccionario = {
    "nombre" : "Python",
    "creador" : "Guido van Rossum"
}

""" for llave in diccionario:
    print("llave:", llave)
    print("valor:", diccionario[llave]) """

for elemento in diccionario.keys(): #Obtenemos las llaves
    print(elemento)

for elemento in diccionario.values(): #Obtenemos los valores
    print (elemento)

for llave,valor in diccionario.items(): #Obtenemos la llave : Valor
    print(llave, valor)

frutas = ["manzana", "naranja", "piña"]
for fruta in frutas:
    x = 0
    for letra in fruta:
        x += 1
    print("fruta: ", fruta)
    print("tiene: ", x, " letras")
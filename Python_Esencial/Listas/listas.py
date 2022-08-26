lenguajes = ["Python", "Java", "JS"]
lista = [1, 2.0, True, "Python", 1]

len(lenguajes) #Longitud de la lista

lenguajes[2]    #Elemento de indice 2
lenguajes[-1]   #Ultimo elemento
lenguajes[0:2]  #Elementos desde el indice 0 hasta el 1

programacion = [lenguajes, "dedicacion", "practica"] #Agregamos la lista lenguajes dentro de la lista programacion

lenguajes [0] = "GO" #Reemplazamos el elemento de indice 0 a el valor "GO"

lenguajes.append("python")  #Agregamos "Python" al final de la lista lenguajes

otros_lenguajes = ["C", "C++"] #Creamos una nueva lista

lenguajes.extend(otros_lenguajes)   #Extendemos la lista lenguajes y le agregamos los elementos de la lista otros_lenguajes

lenguajes.append(otros_lenguajes)   #Agregamos la lista al final de la lista lenguajes


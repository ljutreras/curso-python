set1 = {1,2,3}
set2 = {1,1,1,2,3} #En este caso se mostrara 1,2,3 ya que no muestra datos duplicados
set1.add(4) #agregamos el elemento 4
set1.update([4,5,6]) #Actualizamos el set a 1,2,3,4,5,6
set1.discard(2) #Descartamos el 2 quedando 1,3,4,5,6
set1.remove(3) #Eliminamos el 3
set1.clear() #vaciamos la lista

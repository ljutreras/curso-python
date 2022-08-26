def calcular_primedio(lista):
    assert len(lista) > 0, "La lista está vacia" #Si la condicion es verdadera, enviamos un mensaje personalizado de assert_error
    return sum(lista)/ len(lista)

promedio = calcular_primedio(lista=[1,3,5])
print(promedio)
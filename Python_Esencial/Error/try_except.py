def calcular_primedio(lista):
    assert len(lista) > 0, "La lista está vacia" #Si la condicion es verdadera, enviamos un mensaje personalizado de assert_error
    return sum(lista)/ len(lista)
#Esto es similar al Try Catch en JAVA
#En este caso Except hace la funcion de assert
try:
    promedio = calcular_primedio(lista=[])
    print(promedio)
except AssertionError as assert_error: #Capturamos el assert que se encuentra dentro de la funcion
    print(assert_error) #imprimimos el mensaje del assert capturado de la funcion
except Exception as e: #Obtenemos la excepcion y le damos un alias de nombre e
    print("La funcion no calculó el promedio")
    print(e) #Imprimimos la excepcion capturada

""" except:
    print("La funcion no calculó el promedio") """

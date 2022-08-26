APELLIDO = "Pinto" #Variable global

def funcion():
    print("Mi primera funcion")
    nombre = "Ana" #Variable local
    print(nombre,APELLIDO)

funcion()
print(APELLIDO)
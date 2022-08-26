def perimetro_cuadrado(lado,unidades):
    perimetro = lado*4
    print(f"El perimetro es {perimetro} {unidades}") #Utilizamos la f para colocar los parametros dentro de llaves

perimetro_cuadrado(15, "metros")
perimetro_cuadrado(lado=25, unidades="metro")
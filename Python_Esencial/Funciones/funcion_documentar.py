# Titulo de la descripcion
# Descripcion mas detallada que esta funcion realiza
# Argumentos
#       param (type): que hace?
# Retornos
#       return (type): que hace?

def perimetro_cuadrado(lado):
    """ Calcular el perimetro de un cuadrado.
    
    Esta funcion recibe un valor de un lado de un cuadrado a partir
    de este calcula y retorna su perimetro

    Args:
        lado (int): medida del lado del cuadrado

    Returns:
        perimetro (int): perimetro del cuadrado
    
    """
    perimetro = lado*4
    return perimetro

perimetro_cuadrado(5) #Al pasar el mouse sobre esta linea, te aparece la documentacion creada en la linea 2


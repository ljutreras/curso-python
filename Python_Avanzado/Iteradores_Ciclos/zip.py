nombres = ["Paco", "Emilio", "Javier"]
apellidos = ["Botero", "Tafur", "Quiñonez"]

""" Zip realiza la combinacion de elementos segun el indice en forma de tupla
    es decir, el indice 0 de nombres junto al indice 0 de appellido
    ('Paco' , 'Botero')

    Para esto, ambas listas deben contener la misma cantidad de elementos
    de no ser asi, los elementos sin "Pareja" no seran incluidas
"""
nombre_completo = list(zip(nombres,apellidos))
print(nombre_completo) #[('Paco', 'Botero'), ('Emilio', 'Tafur'), ('Javier', 'Quiñonez')]

nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip) #('Paco', 'Emilio', 'Javier')
print(apellidos_unzip) #('Botero', 'Tafur', 'Quiñonez')

#De esta manera traemos los elementos desde 2 listas unidas desde ZIP
for nombre, apellido in zip(nombres,apellidos):
    print(nombre,apellido)
""" 
    Paco Botero
    Emilio Tafur
    Javier Quiñonez 
"""

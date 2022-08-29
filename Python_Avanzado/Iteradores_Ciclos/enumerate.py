""" 
enumerate(iterable, start=0)
"""

nombres = ["Paco", "Emilio", "Javier"]
nombres_enumerados=enumerate(nombres)
print(list(nombres_enumerados)) #[(0, 'Paco'), (1, 'Emilio'), (2, 'Javier')]

for indice, elemento in enumerate(nombres):
    print(indice,elemento)
""" 
    0 Paco
    1 Emilio
    2 Javier 
"""
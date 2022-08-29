""" 
Desearializacion json.loads
decodificar un JSON, transforma los datos al ser recibidos
"""

import json

with open("./Python_Avanzado/JSON/persona.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

print(type(datos_json))
print(datos_json["nombre"])
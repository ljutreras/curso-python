""" 
Serializacion json.dumps()
convertir los datos en Bytes que seran almacenados o transmitidos entre 
servicios 


"""
import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinonez",
    "edad": 24
}

""" 
objeto_json = json.dumps(persona, indent=2) #Serializamos
with open("./Python_Avanzado/JSON/persona.json", "w") as archivo_json:
    archivo_json.write(objeto_json) #Escribimos nuestro archivo 
"""

with open("./Python_Avanzado/JSON/persona.json", "w") as archivo_json:
    json.dump(persona, archivo_json) 
    #No queda identado como lo hace el DUMPS
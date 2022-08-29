""" 
Comma-Separated Values
Valores separados por comas
nos permite guardar datos de manera sencilla
"""

import csv
import os

ruta = "./Python_Avanzado/CSV/ArchivosCSV/csv_vacio.csv" #Ruta absoluta, poco recomendable por sistemas operativos

#Esto nos garantiza (OS) la usabilidad en diferentes sistemas operativos
ruta_os = os.path.join(os.getcwd(),"csv_vacio.csv")
print(ruta_os)

""" archivo_abierto = open(ruta,"w") # W representa WRITE
writer = csv.writer(archivo_abierto, delimiter=",") #por convencion debe estar dentro de una variable llamada writer, a su vez el delimitador puede ser ', ; TAB, entre otros'
archivo_abierto.close() """
import datetime #Importamos el paquete completo
import datetime as dt #Importamos el paquete y le agregamos un alias, en este caso dt
from datetime import datetime #Importamos un modulo en especifico desde un paquete

hora_actual = datetime.datetime.now() #Paquete.Modulo.Accion()
hora_actual = dt.datetime.now() #AliasPaquete.Modulo.Accion()
hora_actual = datetime.now() #Modulo.Accion()


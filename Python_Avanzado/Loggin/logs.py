import logging

#Lo configuramos con el Level.inicial, Nombre/Ruta del archivo, Modo de sobreescritura "w"
logging.basicConfig(level=logging.DEBUG,filename="./Python_Avanzado/Loggin/ejemplo_logs.log",filemode="w")

logging.debug("Log de debugging")
logging.info("Log de advertencia")
logging.warning("Log de advertencia") #WARNING:root:Log de advertencia
logging.error("Log de error") #ERROR:root:Log de error
logging.critical("Log de error critico") #CRITICAL:root:Log de error critico
#NIVEL : LOGGER : MENSAJE
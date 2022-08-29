from __future__ import division
import logging

#La S nos indica que es un string
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S" #Darle el formato de la fecha
)

nombre = "Paco"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")
""" 
    Asctime        -      LevelName -       Message
2022-08-29 18:03:42,909 - WARNING -     Log de advertencia
2022-08-29 18:03:42,910 - ERROR -       Log de error
2022-08-29 18:03:42,910 - CRITICAL -    Log de error critico 
"""

try:
    division = 2/0
except:
    logging.exception("Division por cero")
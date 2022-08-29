import logging

"""
<Logger logger_personalizado (WARNING)>
WARNING es el valor por defecto
"""

""" logger = logging.getLogger("logger_personalizado")
print(logger)  """


#__main__ hace referencia al modulo actual, en este caso logger_personalizado
logger = logging.getLogger(__name__) #<Logger __main__ (WARNING)>
print(logger) 



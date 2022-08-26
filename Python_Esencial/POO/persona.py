""" class Persona:
    def __init__(self): #La variable SELF representa la instancia de la clase, esta es una buena practica para POO
        print("Estoy en el constructor")

paco = Persona() """

class Persona: #Clase Padre
    def __init__(self, nombre, edad): #Self hace referencia a THIS
        self.nombre = nombre
        self.edad = edad
    def cumplir_anios(self):
        self.edad +=1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")

""" paco = Persona("Paco", 20)
print(paco.nombre)
print(paco.edad) 
paco = Persona("Paco", 20)
paco.cumplir_anios()"""

class Empleado(Persona):

    def __init__(self, horas_totales,nombre,edad): #Cuando creamos un __init__ hace que elmine los atributos de la clase persona
        super(Empleado,self).__init__(nombre,edad) #De esta manera traemos los atributos de la clase padre Persona
        self.horas_totales = horas_totales

    def trabajar(self,horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")

paco = Empleado("Paco",20,30)
paco.trabajar(8)
paco.cumplir_anios()

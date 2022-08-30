# Importamos Tkinter, kit de herramientas de GUI Tk.
from tkinter import *
from tkinter.ttk import *

# importamos desde time el método strftime que devuelve la hora local
from time import strftime

# Creamos una ventana con TK de TKINTER
root = Tk()

# Creamos el titulo de nuestro reloj
root.title("Reloj")


def hora():

    # Obtenemos la Hora local
    datos = strftime('%I:%M:%S %p')  # 12 hrs: Min : Seg  PM/AM

    # Pasamos la hora al label
    label.config(text=datos)

    # Hacemos un retardo de tiempo de 1 segundo, antes de ejecutar el reloj
    label.after(1000, hora)


label = Label(root,
              font=(
                  'Arial', 60
              ),
              padding='50',
              background='orange',
              foreground='black'
              )

# Expando el reloj en el centro de la ventana 
label.pack(expand = True) 
 
# Llamamos a la función hora() 
hora() 
 
# Con el método mainloop() le decimos a Python se detenga hasta aquí y no ejecute nada más  
mainloop()

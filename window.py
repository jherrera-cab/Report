from tkinter import *

#iniciar tkinter
aplication = Tk()

#Tamaño de la ventana
aplication.geometry('1200x630+100+100')

#Deshabilitar boton de maximizar
aplication.resizable(False, False)

#Titulo de la ventana
aplication.title('Ventana Tkinter')

#Color Background
aplication.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplication, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, 
                        text='Sistema de Facturacion', 
                        fg='azure4',
                        font=('Dosis', 58), 
                        bg=('burlywood'), 
                        width=27)
etiqueta_titulo.grid(row=0, column=0)


aplication.mainloop()
#-*- coding:utf-8 -*-
from tkinter import *
#import Tkinter as Tkinter

#funciones de procesamiento
def procesar():
	resultado = peso.get() + altura.get()
	print(resultado)

#Instancia de la clase Tk
ventana = Tk()
ventana.title('Generador de Rutinas')

#Variables que almacenarán los datos
peso = IntVar()
altura = IntVar()
cintura = IntVar()
cuello = IntVar()
genero = IntVar()
genero.set(1)
cadera = IntVar()
actividad = StringVar()
actividad.set("Sedentario")

#generación de widgets
#peso
etiqueta_peso = Label(ventana, text='Peso:')
entrada_peso = Entry(ventana, textvariable=peso)
etiqueta_peso.grid(row=1, column=1)
entrada_peso.grid(row=1, column=2)

#altura
etiqueta_altura = Label(ventana, text='Altura: ')
entrada_altura = Entry(ventana, textvariable=altura)
etiqueta_altura.grid(row=2, column=1)
entrada_altura.grid(row=2, column=2)

#genero
etiqueta_genero = Label(ventana, text='Genero: ')
entrada_genero_1 = Radiobutton(ventana, text='Masculino', variable=genero, value=1)
entrada_genero_2 = Radiobutton(ventana, text='Femenino', variable=genero, value=2)
etiqueta_genero.grid(row=5, column=1)
entrada_genero_1.grid(row=5, column=2)
entrada_genero_2.grid(row=5, column=3)

#actividad
etiqueta_actividad = Label(ventana, text='Actividad: ')
entrada_actividad = OptionMenu(ventana, actividad, "Sedentario", "Moderado", "Activo")
etiqueta_actividad.grid(row=7, column=1)
entrada_actividad.grid(row=7, column=2)

#boton
boton = Button(ventana, text='Procesar', command=procesar, width=20)
boton.grid(row=8, column=3)

#ejecución de ventana
ventana.mainloop()
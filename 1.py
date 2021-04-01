import tkinter 
from tkinter import ttk
from tkinter import filedialog as FileDialog
from tkinter import *
import xml.etree.ElementTree as ET
from xml.dom import minidom

ruta = ''
nombres = []
def test():
    global ruta
    global nombres
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    ruta = str(fichero)
    Label(pestaña1, text = "Ruta:", padx=15 ).place( x = 5, y = 70)
    Label(pestaña1, text = ruta, padx=10).place( x =60, y = 70)
    Label(pestaña1, text = "Combobox para verificar con nombres si es el archivo correcto", padx=10).place( x =5, y = 100)
    tree = ET.parse(ruta)
    root = tree.getroot() 
    combo = ttk.Combobox(pestaña1,state="readonly")
    Label(pestaña1, text = "Nombres Matrices: " , padx=10).place( x = 5, y = 125)
    combo.place(x=140,y = 125)
    values1 = []
    Label(Framecito, text = "Matrices:",bg='yellow').place(x= 260)
    combo1 = ttk.Combobox(Framecito,state="readonly",width = 15)
    combo1.place(x=320)
    for elemen in root.findall('matriz'): 
        nombre = elemen.findtext('nombre')
        values1.append(nombre)
        nombres.append(nombre)
    combo["values"]= values1
    combo1["values"]=nombres
    print(nombres)

def opciones(): 
    global nombres

root = tkinter.Tk()
root.title("Ventana con pestasñas")
root.geometry("680x300")
root.resizable(width=0, height=0)
nb = ttk.Notebook(root)
nb.pack(fill = 'both', expand = 'yes')

pestaña1 = ttk.Frame(nb)
Framecito1 = Frame(pestaña1,bg='yellow',height = 30,width = 900)
Framecito1.place(x=0, y = 0)
Button(Framecito1,text = "Cargar",  bg = 'light blue',command = test, padx=20).place(x=300)
Framecito2 = Frame(pestaña1,bg='yellow',height = 450,width = 900)
Framecito2.place(x=0, y = 50)


pestaña2 = ttk.Frame(nb)
# Frame(pestaña2,bg = 'blue',height = 30,width = 500).place(x=0)
Framecito = Frame(pestaña2,bg='yellow',height = 30,width = 900)
Framecito.place(x=0, y = 0)
Label(Framecito, text = "Operaciones:",bg='yellow').place(x= 0)
combo = ttk.Combobox(Framecito,state="readonly")
combo.place(x=100)
combo["values"]= ["Python", "C", "C++", "Java"]
Button(Framecito,text = "Aceptar",  bg = 'light blue').place(x=600)

    
pestaña3 = ttk.Frame(nb)
pestaña4 = ttk.Frame(nb)

nb.add(pestaña1, text = 'Cargar')
nb.add(pestaña2, text = 'Operaciones')
nb.add(pestaña3, text = 'Pestaña 3')
nb.add(pestaña4, text = 'Pestaña 4')


root.mainloop()
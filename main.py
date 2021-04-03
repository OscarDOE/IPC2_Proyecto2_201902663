from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter 
from tkinter import ttk
import os
from os import remove
import xml.etree.ElementTree as ET
from listamatrices import ListaMatrices
from listamatrices import ListaReportes
from graphviz import Source
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import date,datetime
import time
import webbrowser
from matriz import matriz
from copy import deepcopy
import copy

Matrices = ListaMatrices()
Matrices_Mod = ListaMatrices()
Reportes = ListaReportes()
contador_repo = 1
ruta = ""
valores = []
def cargar_archivo():
    global ruta, valores, nombres
    global Matrices
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Archivos XML","*.xml")])
    ruta = str(pathString)
    label1 = ttk.Label(F1,text= "Ruta:").place(x=2,y=50)
    label1 = ttk.Label(F1,text= ruta).place(x=50,y=50)
    #label1 = ttk.Label(p1,text= "Ruta:").place(x=2,y=100)
    tree = ET.parse(ruta)
    arbol = tree.getroot()
    combo = ttk.Combobox(F1,state="readonly")
    nombre_actual = ""
    filas_actual = 0
    columnas_actual = 0
    posiciony = 80
    imagen = ""
    #t = tkinter.Text(p1,height=625,width=500,background="lightblue")
    #t.pack(side="left", fill= "y")
    #barra.config(command=F1.yview())
    #F1.config(yscrollcommand=barra.set)
    mensaje = '''digraph grafica{
    tbl [
    shape=plaintext
    label=<'''
    for datos in arbol:
        #print("DATOS:",datos)
        for sub in datos:
            if sub.tag == "nombre":
                #print("ENtro a nombre")
                #print("subdd:",sub.tag)
                #print("sub:",sub.text)
                nombre_actual = str(sub.text)
                mensaje += "Nombre: "+nombre_actual+"\n"
                #label1 = ttk.Label(F1,text= "Nombre:").place(x=2,y=posiciony)
                #label1 = ttk.Label(F1,text= nombre_actual).place(x=100,y=posiciony)
                posiciony += 20
            elif sub.tag == "filas":
                #print("ENtro a filas")
                #print("subdd:",sub.tag)
                #print("sub:",sub.text)
                filas_actual = int(sub.text)
                mensaje += "Filas: "+str(filas_actual)+"\n"
                #label1 = ttk.Label(F1,text= "Filas:").place(x=2,y=posiciony)
                #label1 = ttk.Label(F1,text= filas_actual).place(x=100,y=posiciony)
                posiciony += 20
            elif sub.tag == "columnas":
                #print("ENtro a columnas")
                #print("subdd:",sub.tag)
                #print("sub:",sub.text)
                columnas_actual = int(sub.text)
                mensaje += "Columnas: "+str(columnas_actual)+"\n"
                #label1 = ttk.Label(F1,text= " Columnas:").place(x=2,y=posiciony)
                #label1 = ttk.Label(F1,text= columnas_actual).place(x=100,y=posiciony)
                posiciony += 20
            elif sub.tag == "imagen":
                #Matriz.insertar(nombre_actual,filas_actual,columnas_actual)
                nombres.append(nombre_actual)
                Matrices.insertar(nombre_actual, filas_actual, columnas_actual)
                ameter = Matrices.getNodoMatriz(nombre_actual)
                Matrices_Mod.insertar(nombre_actual, filas_actual, columnas_actual)
                ameter_Mod = Matrices_Mod.getNodoMatriz(nombre_actual)
                file = open(str(nombre_actual)+".dot","w") 
                #print("NOMBRE MATRIZ METIENDO:",ameter.nombre)
                #ameter.insertar(fila, columna, valor)
                #print("ENtro a imagen")
                #print("subdd:",sub.tag)
                #print("sub:",sub.text)
                filai = 0
                columnai = 1
                a = ""
                c = sub.text
                d = c.strip()
                #label1 = ttk.Label(F1,text= " Imagen:").place(x=2,y=posiciony)
                salto_linea = 0
                for i in sub.text:
                    if i == "*" or i == "-":
                        a+=i
                        ameter.insertar(filai, columnai, str(i))
                        ameter_Mod.insertar(filai, columnai, str(i))
                        #print("Valor:", i)
                        columnai += 1
                    elif i == "\n":
                        salto_linea += 1
                        filai += 1
                        columnai = 1
                        #print("Salto de LInea ----------------------")
                        #a+=i
                        pass
                    else:
                        #a += i
                        pass    
                paso = ""
                cx = 0
                for i in a:
                    #print("A:",i)
                    if cx < columnas_actual:
                        paso += i
                        cx +=1
                    else:
                        paso += "\n"+i
                        cx = 1
                cx = 1
                cy = 1
                mensaje = '''digraph grafica{\n
                tbl [\n
                shape=plaintext\n
                label=<\n
                <table border="0" cellborder = "0" cellspacing="0">'''
                mensaje += "<tr>"
                x = 0
                while x < len(a):
                    char = a[x]
                    if cx < columnas_actual:
                        if char == "*":
                            mensaje += "<td bgcolor=\"black\">    </td>"
                        else:
                            mensaje+="<td>    </td>"
                        cx += 1
                    else:
                        if cy < filas_actual:

                            if char == "*":
                                mensaje += "<td bgcolor=\"black\">    </td></tr>\n<tr>"
                            else:
                                mensaje+="<td>    </td></tr>\n<tr>"    
                            cx = 1
                            cy +=1        
                        else:
                            if char == "*":
                                mensaje += "<td bgcolor=\"black\">    </td></tr>"
                            else:
                                mensaje+="<td>    </td></tr>"   
                    x += 1                     
                #print("PASO:",paso)        
                #label1 = ttk.Label(F1,text= paso).place(x=100,y=posiciony)
                #posiciony += 200
                mensaje += '''</table>
                    >];
                }'''
                #ameter.recorrerFilas()
                #print("TAMAÑO A:",len(a))
                sumando = filas_actual*15
                posiciony += sumando
                
        #t.insert(tkinter.END, mensaje)
        #label1.insert(tkinter.END, mensaje)
        file.write(mensaje)
        file.close()
        oss = "dot -Tjpg "+ nombre_actual+ ".dot -o "+nombre_actual+".png"
        os.system(oss)
        os.remove(nombre_actual+".dot")
        mensaje = ""
    #print("EMPEZANDO A IMPRIMIR TODAS")        
    #Matrices.mostrardatosf()
            #print("subdd:",sub.tag)
            #print("sub:",sub.text)

            

    root.destroy()



def inicio():
    global raiz, nombres
    global F1
    F1.destroy()
    F1 = Frame(raiz,bg='light blue',height = 30,width = 900)
    F1.place(height=8000,width=6250)
    #F1.place(x=0, y = 0)
    #Button(F1,text = "Cargaddr",  bg = 'green', padx=20).place(x=300)
    c1 = ttk.Combobox(F1,)
    b1F1 = tkinter.Button(F1, text= "Cargar  Archivo", bg= "light green", command=cargar_archivo,width=12)
    b1F1.place(x=0,y=10)
    b2F1 = tkinter.Button(F1, text= "Operaciones Individuales", bg= "light green", command=operaciones,width=20)
    b2F1.place(x=95,y=10)
    b3F1 = tkinter.Button(F1, text= "Operaciones Duales", bg= "light green", command=operacionesd,width=20)
    b3F1.place(x=245,y=10)
    b4F1 = tkinter.Button(F1, text= "Reportes", bg= "light green", command=reportes,width=14)
    b4F1.place(x=395,y=10)
    b5F1 = tkinter.Button(F1, text= "Ayuda", bg= "light green", command=lambda:ayuda(0),width=13)
    b5F1.place(x=503,y=10)
    image2 = Image.open("b123asurero.png")
    photo = ImageTk.PhotoImage(image2)
    #label = tkinter.Label(F1,image=photo)
    #label.img = photo
    #label.place(x=190,y=280)
    b6F1 = tkinter.Button(F1, image=photo, bg= "light green", command=inicio,width=14)
    b6F1.img = photo
    b6F1.place(x=605,y=10)
    if nombres:
        pass
    else:
        label1 = ttk.Label(F1,text="Ruta")
        label1.place(x=2,y=50)
        label1 = ttk.Label(F1,text="No ha ingresado ninguna matriz")
        label1.place(x=50,y=50)
        #barra = tkinter.Scrollbar(F1)
        #barra.pack(side="right",fill="y")

def operaciones():
    global raiz, F1, operacion, Matrices, nombres, ruta
    F1.pack_forget()    
    Fop = tkinter.Tk()
    Fop.geometry('300x500')
    Fop.resizable(width=False,height=False)
    Fop.title('Escogiendo Operación')

    Fra = Frame(Fop,bg='light blue',height = 30,width = 900)
    Fra.place(height=500,width=300)

    var = IntVar()
    R1 = Radiobutton(Fra, text="Rotación Horizontal", 
                    bg='light blue',variable=var, value=1,command=lambda:operaciones2(1))
    R1.pack( side='top' )

    R2 = Radiobutton(Fra, text="Rotación Vertical", 
                    bg='light blue',variable=var, value=2,command=lambda:operaciones2(2))
    R2.pack(side='top' )

    R3 = Radiobutton(Fra, text="Transpuesta", variable=var, 
                    bg='light blue',value=3,command=lambda:operaciones2(3))
    R3.pack(side='top')
    R4 = Radiobutton(Fra, text="Limpiar Zona", variable=var, 
                    bg='light blue',value=4,command=lambda:operaciones2(4))
    R4.pack(side='top')
    R5 = Radiobutton(Fra, text="Agregar Linea Horizontal", variable=var, 
                    bg='light blue',value=5,command=lambda:operaciones2(5))
    R5.pack(side='top')
    R6 = Radiobutton(Fra, text="Agregar Linea Vertical", variable=var, 
                    bg='light blue',value=6,command=lambda:operaciones2(6))
    R6.pack(side='top')
    R7 = Radiobutton(Fra, text="Agregar Rectángulo", variable=var, 
                    bg='light blue',value=7,command=lambda:operaciones2(7))
    R7.pack(side='top')
    R8 = Radiobutton(Fra, text="Agregar Triángulo Rectángulo", 
                    variable=var, bg='light blue',value=8,command=lambda:operaciones2(8))
    R8.pack(side='top')
    x = str(var.get())
    #print("XXXXXXXXXXXXXXXXXXXX.",x)
    #print("NOMBRES:",nombres)
    label = tkinter.Label(Fra,text="Seleccione la matriz que desea operar",bg="light blue")
    label.pack(side="top")
    Com = ttk.Combobox(Fra,state="readonly",width=20)
    Com.pack(side='top')
    Com['values'] = nombres
    matriz_obtenida = Com.current()
    #print(matriz_obtenida)
    bAceptar = tkinter.Button(Fra, text= "Aceptar", width=12, command=lambda:despues_operaciones2(Fop,Com) )
    bAceptar.place(x=0,y=450)
    bSalir = tkinter.Button(Fra, text= "Cancelar",width=12, command=lambda:Cancelar(Fop))
    bSalir.place(x=100,y=450)
    Fra.mainloop()
    
def Cancelar(Frame):
    global operacion
    operacion = 0
    print(operacion)
    Frame.destroy()

def operaciones2(valor):
    global operacion
    operacion = valor
    print(operacion)

def despues_operaciones2(Frame, combo):
    global operacion, nombre_m_1,Matrices_Mod, Matrices, Reportes, contador_repo
    global F1
    nombre_m_1 = combo.get()
    #print("CURRENT:",combo.current())
    #print("GET:",combo.get())

    inicio()
    Frame.destroy()
    #im = PhotoImage(file = nombre_m_1+".gif")
    #FR1 = tkinter.Frame(F1,bg='yellow',)
    
    #FR1.pack(side="top")
    #FR1.place(x=25,y=50)
    image1 = Image.open(nombre_m_1+".png")
    photo = ImageTk.PhotoImage(image1)
    reducida = image1.resize((150,150))
    reducida.save(nombre_m_1+".png")
    image2 = Image.open(nombre_m_1+".png")
    photo = ImageTk.PhotoImage(image2)
    #reducida.show()
    #image1.size = (100,100)
    #print("SIZE:",image1.size)
    #print("SIZE SEGUNDA:",reducida.size)
    label = tkinter.Label(F1,image=photo)
    label.img = photo
    label.place(x=50,y=50)
    label = tkinter.Label(F1, text=nombre_m_1,bg="light blue")
    label.place(x=50,y=230)
    #im = PhotoImage(file=image1)
    #image1 = tkinter.PhotoImage(file="A.gif")
    #Fondo = ttk.Label(F1,image=im).place(x=1,y=1)
    if operacion == 1:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        actual.Horizontal()
        #actual.pruebaf()
        #actual.prueba()
        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        a = ""
        cx = 1
        cy = 1
        a = actual.obtenervaloresporfilas(a)
        a = a.strip()
        #print(a)
        x = 0 
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=250,y=50)
        label = tkinter.Label(F1,text="Resultado de Rotación Horizontal",bg="light blue")
        label.place(x=250,y=230)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Rotación Horizontal -- Matriz usada:"+nombre_m_1)
        contador_repo += 1
        Matrices_Mod = copy.deepcopy(Matrices)
    elif operacion == 2:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        actual.Vertical()
        actual.prueba()
        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        a = ""
        b = []
        cx = 1
        cy = 1
        b = actual.obtenervaloresporcolumnas(b)
        #print(b)
        #print(len(b))
        x = 0
        columnas = actual.columnas
        filas = actual.filas
        for h in range(filas):
            for i in b:     
                print("I:",i)
                #for j in i:
                 #   print("J:",j)
                    #a += j
                a += i[x]
                print(i[x])
                
            x += 1    
            a += "\n"    
        a = a.strip()
        print(a)
        x = 0 
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=250,y=50)
        label = tkinter.Label(F1,text="Resultado de Rotación Vertical",bg="light blue")
        label.place(x=250,y=230)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Rotación Vertical -- Matriz usada:"+nombre_m_1)
        contador_repo += 1
        Matrices_Mod = copy.deepcopy(Matrices)
    elif operacion == 3:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        #actual.Vertical()
        #actual.prueba()
        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        #aux = actual.eColumnas
        #actual.eColumnas = actual.eFilas
        #actual.eFilas = aux
        a = ""
        b = []
        b = actual.Transpuesta(b)
        print(b)
        x = 0
        q = ListaMatrices()
        print(len(b))
        print("SEUNDO:",len(b[1]))
        q.insertar("nueva",len(b) , len(b[0]))
        w = q.getNodoMatriz("nueva")
        for item in (b):
            for j in reversed(item):
                w.insertar(j[2], j[1], j[0])
                print(j)
        actual2 = q.getNodoMatriz("nueva")
        a = actual2.obtenervaloresporfilas(a)
        a = a.strip()
        print(a)
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=250,y=50)
        label = tkinter.Label(F1,text="Resultado de Matriz Transpuesta",bg="light blue")
        label.place(x=250,y=230)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Transpuesta -- Matriz usada:"+nombre_m_1)
        contador_repo += 1
        Matrices_Mod = copy.deepcopy(Matrices)
    elif operacion == 4:
        Fop = tkinter.Tk()
        Fop.geometry("500x100")
        Fop.resizable(width= False,height= False)
        Fop.title("Limpiando Zona")
        Fra = tkinter.Frame(Fop,bg= "light blue")
        Fra.place(height=100,width=500)

        etiquetafinicia = tkinter.Label(Fra,text="FILA INICIO")
        etiquetafinicia.place(x= 10, y=10)
        filainicia = tkinter.Entry(Fra)
        filainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="COLUMNA INICIO")
        etiquetafinicia.place(x= 140, y=10)
        columnainicia = tkinter.Entry(Fra)
        columnainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="FILA TERMINA")
        etiquetafinicia.place(x= 260, y=10)
        filatermina = tkinter.Entry(Fra)
        filatermina.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="COLUMNA TERMINA")
        etiquetafinicia.place(x= 380, y=10)
        columnatermina = tkinter.Entry(Fra)
        columnatermina.pack(side="left")

        bAceptar = tkinter.Button(Fra,text="Aceptar",bg="light green", command=lambda:limpiarz(filainicia.get(),columnainicia.get(),filatermina.get(),columnatermina.get(),Fop))
        bAceptar.place(x=230,y=70)
    elif operacion == 5:
        Fop = tkinter.Tk()
        Fop.geometry("400x100")
        Fop.resizable(width= False,height= False)
        Fop.title("Agregando Barra Horizontal")
        Fra = tkinter.Frame(Fop,bg= "light blue")
        Fra.place(height=100,width=500)

        etiquetafinicia = tkinter.Label(Fra,text="FILA")
        etiquetafinicia.place(x= 10, y=10)
        filainicia = tkinter.Entry(Fra)
        filainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="COLUMNA")
        etiquetafinicia.place(x= 140, y=10)
        columnainicia = tkinter.Entry(Fra)
        columnainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="Numero de Items")
        etiquetafinicia.place(x= 260, y=10)
        filatermina = tkinter.Entry(Fra)
        filatermina.pack(side="left")


        bAceptar = tkinter.Button(Fra,text="Aceptar",bg="light green", command=lambda:limpiarz(filainicia.get(),columnainicia.get(),filatermina.get(),0,Fop))
        bAceptar.place(x=180,y=70)
        
    elif operacion == 6:
        Fop = tkinter.Tk()
        Fop.geometry("400x100")
        Fop.resizable(width= False,height= False)
        Fop.title("Agregando Barra Vertical")
        Fra = tkinter.Frame(Fop,bg= "light blue")
        Fra.place(height=100,width=500)

        etiquetafinicia = tkinter.Label(Fra,text="FILA")
        etiquetafinicia.place(x= 10, y=10)
        filainicia = tkinter.Entry(Fra)
        filainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="COLUMNA")
        etiquetafinicia.place(x= 140, y=10)
        columnainicia = tkinter.Entry(Fra)
        columnainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="Numero de Items")
        etiquetafinicia.place(x= 260, y=10)
        filatermina = tkinter.Entry(Fra)
        filatermina.pack(side="left")


        bAceptar = tkinter.Button(Fra,text="Aceptar",bg="light green", command=lambda:limpiarz(filainicia.get(),columnainicia.get(),filatermina.get(),0,Fop))
        bAceptar.place(x=180,y=70)
    elif operacion == 7:
        Fop = tkinter.Tk()
        Fop.geometry("500x100")
        Fop.resizable(width= False,height= False)
        Fop.title("Agregando Rectángulo")
        Fra = tkinter.Frame(Fop,bg= "light blue")
        Fra.place(height=100,width=500)

        etiquetafinicia = tkinter.Label(Fra,text="FILA INICIO")
        etiquetafinicia.place(x= 10, y=10)
        filainicia = tkinter.Entry(Fra)
        filainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="COLUMNA INICIO")
        etiquetafinicia.place(x= 140, y=10)
        columnainicia = tkinter.Entry(Fra)
        columnainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="ALTURA")
        etiquetafinicia.place(x= 260, y=10)
        filatermina = tkinter.Entry(Fra)
        filatermina.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="BASE")
        etiquetafinicia.place(x= 380, y=10)
        columnatermina = tkinter.Entry(Fra)
        columnatermina.pack(side="left")

        bAceptar = tkinter.Button(Fra,text="Aceptar",bg="light green", command=lambda:limpiarz(filainicia.get(),columnainicia.get(),filatermina.get(),columnatermina.get(),Fop))
        bAceptar.place(x=230,y=70)
        
    elif operacion == 8:
        Fop = tkinter.Tk()
        Fop.geometry("400x100")
        Fop.resizable(width= False,height= False)
        Fop.title("Agregando Trinángulo")
        Fra = tkinter.Frame(Fop,bg= "light blue")
        Fra.place(height=100,width=500)

        etiquetafinicia = tkinter.Label(Fra,text="FILA")
        etiquetafinicia.place(x= 10, y=10)
        filainicia = tkinter.Entry(Fra)
        filainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="COLUMNA")
        etiquetafinicia.place(x= 140, y=10)
        columnainicia = tkinter.Entry(Fra)
        columnainicia.pack(side="left")

        etiquetafinicia = tkinter.Label(Fra,text="LONGITUD")
        etiquetafinicia.place(x= 260, y=10)
        filatermina = tkinter.Entry(Fra)
        filatermina.pack(side="left")


        bAceptar = tkinter.Button(Fra,text="Aceptar",bg="light green", command=lambda:limpiarz(filainicia.get(),columnainicia.get(),filatermina.get(),0,Fop))
        bAceptar.place(x=180,y=70)

    

def limpiarz(fi,ci,ft,ct,Frame):
    global nombre_m_1,Matrices_Mod, operacion, Reportes, contador_repo
    global Matrices
    print(nombre_m_1)
    if operacion == 4:
        if fi < ft and ci < ct:
            actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
            if int(fi) >= 0 and int(ft) <= actual.filas and int(ci) >= 0 and int(ct) <= actual.columnas:
                fi = int(fi)
                ci = int(ci)
                ft = int(ft)
                ct = int(ct)
                actual.recorrerColumnas()
                actual.Limpiar(fi, ci, ft, ct)
                actual.recorrerFilas()
                a = ""
                a = actual.obtenervaloresporfilas(a)
                a = a.strip()
                print(a)
                x = 0 
                mensaje = '''digraph grafica{\n
                tbl [\n
                shape=plaintext\n
                label=<\n
                <table border="0" cellborder = "0" cellspacing="0">\n'''
                mensaje += "<tr>"
                file = open("Resultado.dot","w")
                while x < len(a):
                    char = a[x]
                    if char == "*":
                        mensaje += "<td bgcolor=\"black\">     </td>"
                    elif char == "-":
                        mensaje += "<td>    </td>"
                    elif a[x+1] == None:
                        break  
                    elif char == "\n":
                        mensaje += "</tr>\n<tr>"
                    x += 1
                mensaje += '''</tr></table>
                            >];
                        }'''    
                file.write(mensaje)
                file.close()
                os.system('dot -Tjpg Resultado.dot -o Resultado.png')
                mensaje = ""
                image1 = Image.open("Resultado.png")
                photo = ImageTk.PhotoImage(image1)
                reducida = image1.resize((150,150))
                reducida.save("Resultado.png")
                image2 = Image.open("Resultado.png")
                photo = ImageTk.PhotoImage(image2)
                label = tkinter.Label(F1,image=photo)
                label.img = photo
                label.place(x=250,y=50)
                label = tkinter.Label(F1,text="Resultado de Limpiar Zona",bg="light blue")
                label.place(x=250,y=230)
                today = date.today()
                now = datetime.now()
                x = now.time()
                Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Limpiar Zona -- Matriz usada:"+nombre_m_1)
                contador_repo += 1
                Matrices_Mod = None
                Matrices_Mod = copy.deepcopy(Matrices)
                
                Frame.destroy()
            else:
                today = date.today()
                now = datetime.now()
                x = now.time()
                Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Error: Algún dato mayor que los bordes de la matriz -- Limpiar Zona -- Matriz usada:"+nombre_m_1)
                contador_repo += 1
                messagebox.WARNING(message= "Algun dato es mayor que los bordes de la matriz")        
        else:
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Error: Las filas o columnas finales son menores a las iniciales -- Limpiar Zona -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            messagebox.WARNING(message= "Las filas o las columnas finales son menores a las iniciales")
    elif operacion == 5:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        if actual.filas > int(fi) and actual.columnas > int(ci):
            fi = int(fi)
            ci = int(ci)
            ft = int(ft)
            ct = int(ct)
            actual.recorrerColumnas()
            actual.barraH(fi, ci, ft)
            actual.recorrerFilas()
            a = ""
            a = actual.obtenervaloresporfilas(a)
            a = a.strip()
            print(a)
            x = 0 
            mensaje = '''digraph grafica{\n
            tbl [\n
            shape=plaintext\n
            label=<\n
            <table border="0" cellborder = "0" cellspacing="0">\n'''
            mensaje += "<tr>"
            file = open("Resultado.dot","w")
            while x < len(a):
                char = a[x]
                if char == "*":
                    mensaje += "<td bgcolor=\"black\">     </td>"
                elif char == "-":
                    mensaje += "<td>    </td>"
                elif a[x+1] == None:
                    break  
                elif char == "\n":
                    mensaje += "</tr>\n<tr>"
                x += 1
            mensaje += '''</tr></table>
                        >];
                    }'''    
            file.write(mensaje)
            file.close()
            os.system('dot -Tjpg Resultado.dot -o Resultado.png')
            mensaje = ""
            image1 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image1)
            reducida = image1.resize((150,150))
            reducida.save("Resultado.png")
            image2 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image2)
            label = tkinter.Label(F1,image=photo)
            label.img = photo
            label.place(x=250,y=50)
            label = tkinter.Label(F1,text="Resultado de Agregar Horizontalmente",bg="light blue")
            label.place(x=250,y=230)
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Agregar Horizontalmente -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            Matrices_Mod = None
            Matrices_Mod = copy.deepcopy(Matrices)
            
            Frame.destroy()
        else:
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Error: El nodo desde el que se quiere empezar no existe -- Agregar Horizontalmente -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            messagebox.WARNING(message= "El nodo desde el que quiere iniciar no existe")    
    elif operacion == 6:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        if actual.filas > int(fi) and actual.columnas > int(ci):
            fi = int(fi)
            ci = int(ci)
            ft = int(ft)
            ct = int(ct)
            actual.recorrerColumnas()
            actual.barraV(fi, ci, ft)
            actual.recorrerFilas()
            a = ""
            a = actual.obtenervaloresporfilas(a)
            a = a.strip()
            print(a)
            x = 0 
            mensaje = '''digraph grafica{\n
            tbl [\n
            shape=plaintext\n
            label=<\n
            <table border="0" cellborder = "0" cellspacing="0">\n'''
            mensaje += "<tr>"
            file = open("Resultado.dot","w")
            while x < len(a):
                char = a[x]
                if char == "*":
                    mensaje += "<td bgcolor=\"black\">     </td>"
                elif char == "-":
                    mensaje += "<td>    </td>"
                elif a[x+1] == None:
                    break  
                elif char == "\n":
                    mensaje += "</tr>\n<tr>"
                x += 1
            mensaje += '''</tr></table>
                        >];
                    }'''    
            file.write(mensaje)
            file.close()
            os.system('dot -Tjpg Resultado.dot -o Resultado.png')
            mensaje = ""
            image1 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image1)
            reducida = image1.resize((150,150))
            reducida.save("Resultado.png")
            image2 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image2)
            label = tkinter.Label(F1,image=photo)
            label.img = photo
            label.place(x=250,y=50)
            label = tkinter.Label(F1,text="Resultado de Agregar Verticalmente",bg="light blue")
            label.place(x=250,y=230)
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Agregar Verticalmente -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            Matrices_Mod = None
            Matrices_Mod = copy.deepcopy(Matrices)
            
            Frame.destroy()
        else:
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Error: El nodo desde el que se quiere empezar no existe -- Agregar Verticalmente -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            messagebox.WARNING(message= "El nodo desde el que quiere iniciar no existe")        
    elif operacion == 7:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        if actual.filas > int(fi) and actual.columnas > int(ci):
            fi = int(fi)
            ci = int(ci)
            ft = int(ft)
            ct = int(ct)
            actual.recorrerColumnas()
            actual.cuadro(fi, ci, ft,ct)
            actual.recorrerFilas()
            a = ""
            a = actual.obtenervaloresporfilas(a)
            a = a.strip()
            print(a)
            x = 0
            mensaje = '''digraph grafica{\n
            tbl [\n
            shape=plaintext\n
            label=<\n
            <table border="0" cellborder = "0" cellspacing="0">\n'''
            mensaje += "<tr>"
            file = open("Resultado.dot","w")
            while x < len(a):
                char = a[x]
                if char == "*":
                    mensaje += "<td bgcolor=\"black\">     </td>"
                elif char == "-":
                    mensaje += "<td>    </td>"
                elif a[x+1] == None:
                    break  
                elif char == "\n":
                    mensaje += "</tr>\n<tr>"
                x += 1
            mensaje += '''</tr></table>
                        >];
                    }'''    
            file.write(mensaje)
            file.close()
            os.system('dot -Tjpg Resultado.dot -o Resultado.png')
            mensaje = ""
            image1 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image1)
            reducida = image1.resize((150,150))
            reducida.save("Resultado.png")
            image2 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image2)
            label = tkinter.Label(F1,image=photo)
            label.img = photo
            label.place(x=250,y=50)
            label = tkinter.Label(F1,text="Resultado de Agregar Cuadro",bg="light blue")
            label.place(x=250,y=230)
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Agregar Cuadro -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            Matrices_Mod = None
            Matrices_Mod = copy.deepcopy(Matrices)
            
            Frame.destroy() 
        
    elif operacion == 8:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        if actual.filas > int(fi) and actual.columnas > int(ci):
            fi = int(fi)
            ci = int(ci)
            ft = int(ft)
            ct = int(ct)
            actual.recorrerColumnas()
            actual.triangulo(fi,ci,ft)
            actual.recorrerFilas()
            a = ""
            a = actual.obtenervaloresporfilas(a)
            a = a.strip()
            print(a)
            x = 0 
            mensaje = '''digraph grafica{\n
            tbl [\n
            shape=plaintext\n
            label=<\n
            <table border="0" cellborder = "0" cellspacing="0">\n'''
            mensaje += "<tr>"
            file = open("Resultado.dot","w")
            while x < len(a):
                char = a[x]
                if char == "*":
                    mensaje += "<td bgcolor=\"black\">     </td>"
                elif char == "-":
                    mensaje += "<td>    </td>"
                elif a[x+1] == None:
                    break  
                elif char == "\n":
                    mensaje += "</tr>\n<tr>"
                x += 1
            mensaje += '''</tr></table>
                        >];
                    }'''    
            file.write(mensaje)
            file.close()
            os.system('dot -Tjpg Resultado.dot -o Resultado.png')
            mensaje = ""
            image1 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image1)
            reducida = image1.resize((150,150))
            reducida.save("Resultado.png")
            image2 = Image.open("Resultado.png")
            photo = ImageTk.PhotoImage(image2)
            label = tkinter.Label(F1,image=photo)
            label.img = photo
            label.place(x=250,y=50)
            label = tkinter.Label(F1,text="Resultado de Agregar Triángulo",bg="light blue")
            label.place(x=250,y=230)
            today = date.today()
            now = datetime.now()
            x = now.time()
            Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Agregar Triángulo -- Matriz usada:"+nombre_m_1)
            contador_repo += 1
            Matrices_Mod = copy.deepcopy(Matrices)            

            Frame.destroy() 
        

def operacionesd():
    global raiz, F1, operacion, Matrices, nombres
    F1.pack_forget()    
    Fop = tkinter.Tk()
    Fop.geometry('300x500')
    Fop.resizable(width=False,height=False)
    Fop.title('Escogiendo Operación')

    Fra = Frame(Fop,bg='light blue')
    Fra.place(height=500,width=300)

    var = IntVar()
    R1 = Radiobutton(Fra, text="Unión", 
                    bg='light blue',variable=var, value=1,command=lambda:operaciones2(9))
    R1.pack( side='top' )

    R2 = Radiobutton(Fra, text="Intersección", 
                    bg='light blue',variable=var, value=2,command=lambda:operaciones2(10))
    R2.pack(side='top' )

    R3 = Radiobutton(Fra, text="Diferencia", variable=var, 
                    bg='light blue',value=3,command=lambda:operaciones2(11))
    R3.pack(side='top')
    R4 = Radiobutton(Fra, text="Diferencia Simétrica", variable=var, 
                    bg='light blue',value=4,command=lambda:operaciones2(12))
    R4.pack(side='top')
    
    x = str(var.get())
    #print("XXXXXXXXXXXXXXXXXXXX.",x)
    #print("NOMBRES:",nombres)
    label = tkinter.Label(Fra,text="Seleccione la matriz que desea operar",bg="light blue")
    label.pack(side="top")
    Com = ttk.Combobox(Fra,state="readonly",width=20)
    Com.pack(side='top')
    Com['values'] = nombres
    matriz_obtenida = Com.current()

    label = tkinter.Label(Fra,text="Seleccione la segunda matriz que desea operar",bg="light blue")
    label.pack(side="top")
    Com1 = ttk.Combobox(Fra,state="readonly",width=20)
    Com1.pack(side='top')
    Com1['values'] = nombres
    matriz_obtenida = Com1.current()
    #print(matriz_obtenida)
    bAceptar = tkinter.Button(Fra, text= "Aceptar", width=12, command=lambda:despues_operaciones2d(Fop,Com,Com1) )
    bAceptar.place(x=0,y=450)
    bSalir = tkinter.Button(Fra, text= "Cancelar",width=12, command=lambda:Cancelar(Fop))
    bSalir.place(x=100,y=450)
    Fra.mainloop()

def despues_operaciones2d(Frame, combo1, combo2):
    global operacion, nombre_m_1, nombre_m_2,Matrices_Mod, Matrices, Reportes, contador_repo
    global F1
    nombre_m_1 = combo1.get()
    nombre_m_2 = combo2.get()
    inicio()
    Frame.destroy()
    image1 = Image.open(nombre_m_1+".png")
    photo = ImageTk.PhotoImage(image1)
    reducida = image1.resize((150,150))
    reducida.save(nombre_m_1+".png")
    image2 = Image.open(nombre_m_1+".png")
    photo = ImageTk.PhotoImage(image2)
    label = tkinter.Label(F1,image=photo)
    label.img = photo
    label.place(x=50,y=50)
    label = tkinter.Label(F1, text=nombre_m_1,bg="light blue")
    label.place(x=50,y=230)
    
    image1 = Image.open(nombre_m_2+".png")
    photo = ImageTk.PhotoImage(image1)
    reducida = image1.resize((150,150))
    reducida.save(nombre_m_2+".png")
    image2 = Image.open(nombre_m_2+".png")
    photo = ImageTk.PhotoImage(image2)
    label = tkinter.Label(F1,image=photo)
    label.img = photo
    label.place(x=250,y=50)
    label = tkinter.Label(F1, text=nombre_m_2,bg="light blue")
    label.place(x=250,y=230)
    if operacion == 9:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        actual2 = Matrices_Mod.getNodoMatriz(nombre_m_2)
        mayorf = 0
        mayorc = 0
        if actual.filas > actual2.filas:
            mayorf = actual.filas
        else:
            mayorf = actual2.filas    
        if actual.columnas > actual2.columnas:
            mayorc = actual.columnas
        else:
            mayorc = actual2.columnas    
        momentanea = matriz("r", mayorf, mayorc)
        momentanea.llenar()
        momentanea.union(actual, actual2)
        a = ""
        a = momentanea.obtenervaloresporfilas(a)
        print(a)
        a = a.strip()

        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        x = 0
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=190,y=280)
        label = tkinter.Label(F1,text="Resultado de Union entre ambas matrices",bg="light blue")
        label.place(x=210,y=450)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Unión -- Matrices usadas:"+nombre_m_1+","+ nombre_m_2)
        contador_repo += 1
        #Matrices_Mod = Matrices
        
        Frame.destroy()
        
        
    elif operacion == 10:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        actual2 = Matrices_Mod.getNodoMatriz(nombre_m_2)
        mayorf = 0
        mayorc = 0
        if actual.filas > actual2.filas:
            mayorf = actual.filas
        else:
            mayorf = actual2.filas    
        if actual.columnas > actual2.columnas:
            mayorc = actual.columnas
        else:
            mayorc = actual2.columnas    
        momentanea = matriz("r", mayorf, mayorc)
        momentanea.llenar()
        momentanea.interseccion(actual, actual2)
        a = ""
        a = momentanea.obtenervaloresporfilas(a)
        print(a)
        a = a.strip()
        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        x = 0
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=190,y=280)
        label = tkinter.Label(F1,text="Resultado de Intersección entre ambas matrices",bg="light blue")
        label.place(x=210,y=450)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Intersección -- Matrices usadas:"+nombre_m_1+","+ nombre_m_2)
        contador_repo += 1
        #Matrices_Mod = Matrices
        
        Frame.destroy()
    elif operacion == 11:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        actual2 = Matrices_Mod.getNodoMatriz(nombre_m_2)
        mayorf = 0
        mayorc = 0
        if actual.filas > actual2.filas:
            mayorf = actual.filas
        else:
            mayorf = actual2.filas    
        if actual.columnas > actual2.columnas:
            mayorc = actual.columnas
        else:
            mayorc = actual2.columnas    
        momentanea = matriz("r", mayorf, mayorc)
        momentanea.llenar()
        momentanea.diferencia(actual, actual2)
        a = ""
        a = momentanea.obtenervaloresporfilas(a)
        print(a)
        a = a.strip()
        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        x = 0
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=190,y=280)
        label = tkinter.Label(F1,text="Resultado de Diferencia entre ambas matrices",bg="light blue")
        label.place(x=210,y=450)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Diferencia -- Matrices usadas:"+nombre_m_1+","+ nombre_m_2)
        contador_repo += 1
        #Matrices_Mod = Matrices
        
        Frame.destroy()
    elif operacion == 12:
        actual = Matrices_Mod.getNodoMatriz(nombre_m_1)
        actual2 = Matrices_Mod.getNodoMatriz(nombre_m_2)
        mayorf = 0
        mayorc = 0
        if actual.filas > actual2.filas:
            mayorf = actual.filas
        else:
            mayorf = actual2.filas    
        if actual.columnas > actual2.columnas:
            mayorc = actual.columnas
        else:
            mayorc = actual2.columnas    
        momentanea = matriz("r", mayorf, mayorc)
        momentanea.llenar()
        momentanea.difsimetrica(actual, actual2)
        a = ""
        a = momentanea.obtenervaloresporfilas(a)
        print(a)
        a = a.strip()
        mensaje = '''digraph grafica{\n
        tbl [\n
        shape=plaintext\n
        label=<\n
        <table border="0" cellborder = "0" cellspacing="0">\n'''
        mensaje += "<tr>"
        x = 0
        file = open("Resultado.dot","w")
        while x < len(a):
            char = a[x]
            if char == "*":
                mensaje += "<td bgcolor=\"black\">     </td>"
            elif char == "-":
                mensaje += "<td>    </td>"
            elif a[x+1] == None:
                break  
            elif char == "\n":
                mensaje += "</tr>\n<tr>"
            x += 1
        mensaje += '''</tr></table>
                    >];
                }'''    
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg Resultado.dot -o Resultado.png')
        mensaje = ""
        image1 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image1)
        reducida = image1.resize((150,150))
        reducida.save("Resultado.png")
        image2 = Image.open("Resultado.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=190,y=280)
        label = tkinter.Label(F1,text="Resultado de Diferencia Simétrica entre ambas matrices",bg="light blue")
        label.place(x=210,y=450)
        today = date.today()
        now = datetime.now()
        x = now.time()
        Reportes.insertar(contador_repo, str(today)+"---"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" Intersección -- Matrices usadas:"+nombre_m_1+","+ nombre_m_2)
        contador_repo += 1
        #Matrices_Mod = Matrices
        Frame.destroy()
    
def reportes():
    global contador_repo, Reportes
    if Reportes is not None:
        mensaje = """<html>
        <head>
        
        <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        th, td {
        padding: 5px;
        text-align: left;    
        }
        body {
            color: black;
            background-color: lightgreen;
        }
        div {
            padding: 8px 20px;
            margin: 54px -2px;
            box-shadow: none!important;
            border: solid blue;
            
        }
        table {
            padding: 30px;
        }
        table, th, td, tbody, thead {
        border: 0px;
        border-collapse: collapse;
        }
        th, td {
        padding: 5px;
        text-align: left;    
        }
        </style>
        <title>Proyecto 2 [IPC2]</title>
        </head>
        
        <body><h1 style="color:black"><center>Proyecto 2 Introducción a la Programación y Computación 2 (D)</center></h1>
            <h1 style = \"color:red\"><center> Reporte de Actividades</center></h1>
        """
        a = ""
        a = Reportes.obtenerdatos(a)
        x = 0
        individual = ""
        while x < len(a):
            char = a[x]
            if char == "\n":
                print("SALTO DE LINEA")
                mensaje += "<h2 style=\"color:black\">"+individual+"</h2>"
                print(individual)
                individual = ""
            else:
                individual += char
            x += 1


        print(a)
        mensaje += """</body>
        </html>"""
        f = open('[IPC2]Reportes.html','w',encoding='utf-8')
        f.write(mensaje)
        f.close()
        webbrowser.open_new_tab('[IPC2]Reportes.html')
        
    else:
        print("ESTA VACIA LA LISTA")
        pass


    

def ayuda(a):
    global raiz, F1
    if a == 0:
        inicio()
        byo = tkinter.Button(F1, text="Información del Creador",bg= "light green", command=lambda:ayuda(1))
        byo.place(x=60,y=150)
        bensayo = tkinter.Button(F1, text="Desplegar Documentación del Programa",bg= "light green", command=lambda:os.startfile("Ensayo_Proyecto2[IPC2].pdf"))
        bensayo.place(x=300,y=150)
        
    else:
        label = tkinter.Label(F1,text="NOMBRE: OSCAR DANIEL OLIVA ESPAÑA",bg="light blue")
        label.place(x=30,y=250)
        label = tkinter.Label(F1,text="CARNÉT: 201902663",bg="light blue")
        label.place(x=30,y=300)
        label = tkinter.Label(F1,text="FACULTAD: INGENIERÍA EN CIENCIAS Y SISTEMAS",bg="light blue")
        label.place(x=30,y=350)
        label = tkinter.Label(F1,text="SEMESTRE: 4to.",bg="light blue")
        label.place(x=30,y=400)




valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
nombre_m_1 = ""
nombre_m_2 = ""
nombres = []
operacion = 0
raiz = tkinter.Tk()
raiz.geometry('625x500')
raiz.resizable(width=True,height=True)
raiz.title('IPC 2 Proyecto 2')
#nb = ttk.Notebook(raiz,width=625)
#nb.pack(fill=BOTH, expand=TRUE)
#tinfo = Entry(self.raiz, width=50,font=("Calibri 20"))

#p1 = ttk.Frame(nb)
#nb.add(p1,text='Cargar Archivos')
F1 = Frame(raiz,bg='light blue')
#F1.place(x=50,y=0)
F1.place(height=8000,width=6250)
#F1.place(x=0, y = 0)
#Button(F1,text = "Cargaddr",  bg = 'green', padx=20).place(x=300)
c1 = ttk.Combobox(F1,)
b1F1 = tkinter.Button(F1, text= "Cargar  Archivo", bg= "light green", command=cargar_archivo,width=12)
b1F1.place(x=0,y=10)
b2F1 = tkinter.Button(F1, text= "Operaciones Individuales", bg= "light green", command=operaciones,width=20)
b2F1.place(x=95,y=10)
b3F1 = tkinter.Button(F1, text= "Operaciones Duales", bg= "light green", command=operacionesd,width=20)
b3F1.place(x=245,y=10)
b4F1 = tkinter.Button(F1, text= "Reportes", bg= "light green", command=inicio,width=14)
b4F1.place(x=395,y=10)
b5F1 = tkinter.Button(F1, text= "Ayuda", bg= "light green", command=lambda:ayuda(0),width=13)
b5F1.place(x=503,y=10)

image2 = Image.open("b123asurero.png")
photo = ImageTk.PhotoImage(image2)

b6F1 = tkinter.Button(F1, image=photo, bg= "light green", command=inicio,width=14)
b6F1.img = photo
b6F1.place(x=605,y=10)

label1 = ttk.Label(F1,text="Ruta")
label1.place(x=2,y=50)
label1 = ttk.Label(F1,text="No ha ingresado ninguna matriz")
label1.place(x=50,y=50)

raiz.mainloop()
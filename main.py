from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter 
from tkinter import ttk
import os
import xml.etree.ElementTree as ET
from listamatrices import ListaMatrices
from graphviz import Source
from PIL import ImageTk, Image
from tkinter import messagebox

Matrices = ListaMatrices()
Matrices_Mod = ListaMatrices()
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
        print("DATOS:",datos)
        for sub in datos:
            if sub.tag == "nombre":
                print("ENtro a nombre")
                print("subdd:",sub.tag)
                print("sub:",sub.text)
                nombre_actual = str(sub.text)
                mensaje += "Nombre: "+nombre_actual+"\n"
                label1 = ttk.Label(F1,text= "Nombre:").place(x=2,y=posiciony)
                label1 = ttk.Label(F1,text= nombre_actual).place(x=100,y=posiciony)
                posiciony += 20
            elif sub.tag == "filas":
                print("ENtro a filas")
                print("subdd:",sub.tag)
                print("sub:",sub.text)
                filas_actual = int(sub.text)
                mensaje += "Filas: "+str(filas_actual)+"\n"
                label1 = ttk.Label(F1,text= "Filas:").place(x=2,y=posiciony)
                label1 = ttk.Label(F1,text= filas_actual).place(x=100,y=posiciony)
                posiciony += 20
            elif sub.tag == "columnas":
                print("ENtro a columnas")
                print("subdd:",sub.tag)
                print("sub:",sub.text)
                columnas_actual = int(sub.text)
                mensaje += "Columnas: "+str(columnas_actual)+"\n"
                label1 = ttk.Label(F1,text= " Columnas:").place(x=2,y=posiciony)
                label1 = ttk.Label(F1,text= columnas_actual).place(x=100,y=posiciony)
                posiciony += 20
            elif sub.tag == "imagen":
                #Matriz.insertar(nombre_actual,filas_actual,columnas_actual)
                nombres.append(nombre_actual)
                Matrices.insertar(nombre_actual, filas_actual, columnas_actual)
                ameter = Matrices.getNodoMatriz(nombre_actual)
                Matrices_Mod.insertar(nombre_actual, filas_actual, columnas_actual)
                ameter_Mod = Matrices_Mod.getNodoMatriz(nombre_actual)
                file = open(str(nombre_actual)+".dot","w") 
                print("NOMBRE MATRIZ METIENDO:",ameter.nombre)
                #ameter.insertar(fila, columna, valor)
                print("ENtro a imagen")
                print("subdd:",sub.tag)
                print("sub:",sub.text)
                filai = 0
                columnai = 1
                a = ""
                c = sub.text
                d = c.strip()
                label1 = ttk.Label(F1,text= " Imagen:").place(x=2,y=posiciony)
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
                print("PASO:",paso)        
                label1 = ttk.Label(F1,text= paso).place(x=100,y=posiciony)
                #posiciony += 200
                mensaje += '''</table>
                    >];
                }'''
                #ameter.recorrerFilas()
                print("TAMAÑO A:",len(a))
                sumando = filas_actual*15
                posiciony += sumando
                
        #t.insert(tkinter.END, mensaje)
        #label1.insert(tkinter.END, mensaje)
        file.write(mensaje)
        file.close()
        oss = "dot -Tjpg "+ nombre_actual+ ".dot -o "+nombre_actual+".png"
        os.system(oss)
        mensaje = ""
    print("EMPEZANDO A IMPRIMIR TODAS")        
    #Matrices.mostrardatosf()
            #print("subdd:",sub.tag)
            #print("sub:",sub.text)

            

    root.destroy()



def inicio():
    global raiz
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
    b4F1 = tkinter.Button(F1, text= "Reportes", bg= "light green", command=inicio,width=14)
    b4F1.place(x=395,y=10)
    b5F1 = tkinter.Button(F1, text= "Ayuda", bg= "light green", command=inicio,width=14)
    b5F1.place(x=503,y=10)


    #label1 = ttk.Label(F1,text="Ruta")
    #label1.place(x=2,y=50)
    #label1 = ttk.Label(F1,text="No ha ingresado ninguna matriz")
    #label1.place(x=50,y=50)
    #barra = tkinter.Scrollbar(F1)
    #barra.pack(side="right",fill="y")

def operaciones():
    global raiz, F1, operacion, Matrices, nombres
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
    print("XXXXXXXXXXXXXXXXXXXX.",x)
    print("NOMBRES:",nombres)
    Com = ttk.Combobox(Fra,state="readonly",width=20)
    Com.pack(side='top')
    Com['values'] = nombres
    matriz_obtenida = Com.current()
    print(matriz_obtenida)
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
    global operacion, nombre_m_1,Matrices_Mod, Matrices
    global F1
    nombre_m_1 =  combo.get()
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
    reducida.save(nombre_m_1+"redux.png")
    image2 = Image.open(nombre_m_1+"redux.png")
    photo = ImageTk.PhotoImage(image2)
    #reducida.show()
    #image1.size = (100,100)
    print("SIZE:",image1.size)
    print("SIZE SEGUNDA:",reducida.size)
    label = tkinter.Label(F1,image=photo)
    label.img = photo
    label.place(x=50,y=50)
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
        reducida.save("Reducidaredux.png")
        image2 = Image.open("Reducidaredux.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=250,y=50)
        Matrices_Mod = Matrices
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
        print(b)
        print(len(b))
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
        reducida.save("Reducidaredux.png")
        image2 = Image.open("Reducidaredux.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=250,y=50)
        Matrices_Mod = Matrices
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
        reducida.save("Reducidaredux.png")
        image2 = Image.open("Reducidaredux.png")
        photo = ImageTk.PhotoImage(image2)
        label = tkinter.Label(F1,image=photo)
        label.img = photo
        label.place(x=250,y=50)
        Matrices_Mod = Matrices
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
        pass    

    

def limpiarz(fi,ci,ft,ct,Frame):
    if fi < ft and ci < ct:

        print(fi)
        print(ci)
        print(ft)
        print(ct)
        Frame.destroy()
    else:
        messagebox.WARNING(message= "Las filas o las columnas finales son menores a las iniciales")
    pass
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
    print("XXXXXXXXXXXXXXXXXXXX.",x)
    bAceptar = tkinter.Button(Fra, text= "Aceptar", width=12)
    bAceptar.place(x=0,y=450)
    bSalir = tkinter.Button(Fra, text= "Cancelar",width=12)
    bSalir.place(x=100,y=450)
    print("NOMBRES:",nombres)
    Com = ttk.Combobox(Fra,state="readonly",width=20)
    Com.pack(side='top')
    Com['values'] = nombres
    Fra.mainloop()


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
b5F1 = tkinter.Button(F1, text= "Ayuda", bg= "light green", command=inicio,width=14)
b5F1.place(x=503,y=10)


label1 = ttk.Label(F1,text="Ruta")
label1.place(x=2,y=50)
label1 = ttk.Label(F1,text="No ha ingresado ninguna matriz")
label1.place(x=50,y=50)
#b2F1 = tkinter.Button(F1, text= "Y", bg= "light blue")
#b2F1.place(x=2,y=0)
#barra = tkinter.Scrollbar(F1)
#barra.pack(side="right",fill="y")



raiz.mainloop()


                            
    

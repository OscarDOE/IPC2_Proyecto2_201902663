from nodos import nodoEncabezado,Nodo
from encabezado import listaEncabezado

class matriz:
    def __init__(self, nombre, filas, columnas):
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado()
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.siguiente = None
        self.anterior = None

    def insertar(self, fila, columna, valor):
        nuevo = Nodo(fila, columna, valor)
        #Insercion encabezado por filas
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquieda = actual       
        # insercion encabezado por columnas
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = nodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual


    def recorrerFilas(self):
        eFila = self.eFilas.primero
        print("\n****************************** Recorrido por Filas ********************")
        while eFila != None:
            actual = eFila.accesoNodo            
            print("\n Fila "+str(actual.fila))
            print("Columna:  Valor")
            while actual != None:
                print(str(actual.columna)+"            "+actual.valor)
                actual = actual.derecha

            eFila = eFila.siguiente

        print("\n****************************** Fin Recorrido por Filas ********************")
    
    def obtenervaloresporfilas(self,a):
        eFila = self.eFilas.primero
        print("\n****************************** Recorrido por Filas ********************")
        while eFila != None:
            actual = eFila.accesoNodo            
            print("\n Fila "+str(eFila.id))
            print("Columna:  Valor:          FILA:")
            while actual != None:
                print(str(actual.columna)+"            "+actual.valor+"         "+str(actual.fila))
                a += str(actual.valor)
                actual = actual.derecha

            a += "\n"
            eFila = eFila.siguiente
        print("\n****************************** Fin Recorrido por Filas ********************")
        return a    
    
   
    
    def pruebaf(self):
        eFila = self.eFilas.primero
        print("\n****************************** Recorrido por Filas DE PRUEBA ********************")
        while eFila != None:
            actual = eFila.accesoNodo            
            print(str(actual.fila))
            
            while actual != None:
                print(actual.valor)
                actual = actual.derecha

            eFila = eFila.siguiente

        print("\n****************************** Fin Recorrido por Filas DE PRUEBA ********************")
    
    
    def recorrerColumnas(self):
        eColumna = self.eColumnas.primero
        print("\n****************************** Recorrido por Columnas ********************")
        while eColumna != None:
            actual = eColumna.accesoNodo      
            x = eColumna.id      
            print("\n Columna "+str(actual.columna))
            print("Fila:  Valor                                    : id")
            while actual != None:
                print(str(actual.fila)+"            "+actual.valor+"                   "+str(x))
                actual = actual.abajo

            eColumna = eColumna.siguiente

        print("\n****************************** Fin Recorrido por Columnas ********************")
    
    def obtenervaloresporcolumnas(self,b):
        eColumna = self.eColumnas.primero
        a = []
        print("\n****************************** Recorrido por Columnas ********************")
        while eColumna != None:
            actual = eColumna.accesoNodo      
            x = eColumna.id      
            print("\n Columna "+str(actual.columna))
            print("Fila:  Valor                                    : id")
            x = 0
            while actual != None:
                a.append(actual.valor)
                print(str(actual.fila)+"            "+actual.valor+"                   ")
                actual = actual.abajo
            b.append(a)
            a = []
            eColumna = eColumna.siguiente

        print("\n****************************** Fin Recorrido por Columnas ********************")
        return b
    
    def prueba(self):
        eColumna = self.eColumnas.primero
        print("\n****************************** Recorrido por Columnas DE PRUEBA ********************")
        while eColumna != None:
            actual = eColumna.accesoNodo      
            x = eColumna.id      
            print( str(eColumna.id))
            while actual != None:
                print("Columna: "+str(actual.columna)+" FILA: "+str(actual.fila)+" Valor: "+actual.valor)
                actual = actual.abajo

            eColumna = eColumna.siguiente

        print("\n****************************** Fin Recorrido por Columnas DE PRUEBA ********************")

    def Horizontal(self):
        #eFila = self.eFilas.primero
        print("************************** HACIENDO HORIZONTAL ************************")
        filas = self.filas
        columnas = self.columnas
        #eFila.id
        a = 1
        b = filas
        print("A:",a)    
        print("B:",b)    
        if b % 2 == 0:
            while a < b:
                if a == 1:
                    pass
                arriba = self.eFilas.getEncabezado(a)
                abajo = self.eFilas.getEncabezado(b)
                print("ARRIBA ANTES:",arriba.id)
                print("ABAJO ANTES:",abajo.id)
                if a == 1:
                    pass
                elif a == (b-1):
                    aux = arriba.siguiente
                    aux2 = arriba.anterior
                    aux3 = abajo.siguiente
                    aux4 = abajo.anterior
                    arriba.anterior.siguiente = abajo

                    abajo.siguiente.anterior = arriba

                    abajo.anterior = arriba.anterior

                    arriba.siguiente = abajo.siguiente
                    arriba.anterior = abajo
                    abajo.siguiente = arriba
                    auxnum = arriba.id
                    arriba.id = abajo.id
                    abajo.id = auxnum


                    break
                else:
                    pass
                aux = arriba.siguiente
                aux2 = arriba.anterior
                aux3 = abajo.siguiente
                aux4 = abajo.anterior
                
                arriba.siguiente.anterior = abajo
                rrcolumnas = self.eColumnas.primero
                if arriba == self.eFilas.primero:
                    self.eFilas.primero = abajo
                    access = arriba.accesoNodo
                    access2 = abajo.accesoNodo
                    while access != None:
                        #if access == self.eColumnas.primero.accesoNodo:
                           # self.eColumnas.primero.accesoNodo = access2
                        rrcolumnas.accesoNodo = access2
                        au1 = access.abajo
                        au2 = access2.arriba

                        access.abajo.arriba = access2

                        access2.arriba.abajo = access
                        access.arriba = au2
                        access2.abajo = au1
                        access.abajo = None
                        access2.arriba = None
                        auxf = access.fila
                        access.fila = access2.fila
                        access2.fila = auxf                        
                        print("VVVVVVV  COLUMNA:",access.columna, "VVVVVV FILA:",access.fila)
                        print("BBBBBBB  COLUMNA:",access2.columna, "BBBBBB FILA:",access2.fila)
                        rrcolumnas = rrcolumnas.siguiente
                        access = access.derecha
                        access2 = access2.derecha


                    print("ES PRiMERO")
                else:
                    arriba.anterior.siguiente = abajo
                    #print(arriba.anterior.siguiente.id)
                if b == filas:
                    print("ES ULTIMO")
                    pass
                else:
                    abajo.siguiente.anterior = arriba

                abajo.anterior.siguiente = arriba

                arriba.siguiente = abajo.siguiente

                arriba.anterior = abajo.anterior

                abajo.siguiente = aux

                abajo.anterior = aux2

                auxnum = arriba.id
                arriba.id = abajo.id
                abajo.id = auxnum
                access = arriba.accesoNodo
                access2 = abajo.accesoNodo
                '''while access != None:
                    a1.abajo.arriba = a2
                    if a == 1:
                        self.eFilas.primero = a2
                        pass
                    else:
                        a1.arriba.abajo = a2
                    if b == filas:
                        a2.arriba.abajo = a1
                    else:
                        a2.abajo.arriba = a1
                        a2.arriba.abajo = a1
                    a1 = a1.derecha
                    a2 = a2.derecha'''
                print("ARRIBA:",arriba.id)
                print("ABAJO:",abajo.id)
                a += 1
                b -= 1
                print("A CAMBIARA A :",a, "    B CAMBIARA A :",b)

            print("ES PAR")
        else:
            while a < b:
                arriba = self.eFilas.getEncabezado(a)
                abajo = self.eFilas.getEncabezado(b)
                print("ARRIBA ANTES:",arriba.id)
                print("ABAJO ANTES:",abajo.id)
                aux = arriba.siguiente
                aux2 = arriba.anterior
                aux3 = abajo.siguiente
                aux4 = abajo.anterior
                
                arriba.siguiente.anterior = abajo
                rrcolumnas = self.eColumnas.primero
                if arriba == self.eFilas.primero:
                    self.eFilas.primero = abajo
                    access = arriba.accesoNodo
                    access2 = abajo.accesoNodo
                    while access != None:
                        #if access == self.eColumnas.primero.accesoNodo:
                           # self.eColumnas.primero.accesoNodo = access2
                        rrcolumnas.accesoNodo = access2
                        au1 = access.abajo
                        au2 = access2.arriba

                        access.abajo.arriba = access2

                        access2.arriba.abajo = access
                        access.arriba = au2
                        access2.abajo = au1
                        access.abajo = None
                        access2.arriba = None
                        auxf = access.fila
                        access.fila = access2.fila
                        access2.fila = auxf                        
                        print("VVVVVVV  COLUMNA:",access.columna, "VVVVVV FILA:",access.fila)
                        print("BBBBBBB  COLUMNA:",access2.columna, "BBBBBB FILA:",access2.fila)
                        rrcolumnas = rrcolumnas.siguiente
                        access = access.derecha
                        access2 = access2.derecha
                    print("ES PRiMERO")
                else:
                    arriba.anterior.siguiente = abajo
                    #print(arriba.anterior.siguiente.id)    
                if b == filas:
                    print("ES ULTIMO")
                    pass
                else:
                    abajo.siguiente.anterior = arriba
                abajo.anterior.siguiente = arriba

                arriba.siguiente = abajo.siguiente

                arriba.anterior = abajo.anterior

                abajo.siguiente = aux

                abajo.anterior = aux2

                auxnum = arriba.id
                arriba.id = abajo.id
                abajo.id = auxnum
                access = arriba.accesoNodo
                access2 = abajo.accesoNodo
                a += 1 
                b -= 1   
                print("ARRIBA:",arriba.id)
                print("ABAJO:",abajo.id)
                a += 1
                b -= 1
                print("A CAMBIARA A :",a, "    B CAMBIARA A :",b)


            print("ES IMPAR")
            pass
    def Vertical(self):
        filas = self.filas
        columnas = self.columnas
        a = 1
        b = columnas
        if b % 2 == 0:
            while a < b:
                arriba = self.eColumnas.getEncabezado(a)
                abajo = self.eColumnas.getEncabezado(b)
                print("ARRIBA ANTES:",arriba.id)
                print("ABAJO ANTES:",abajo.id)
                if a == 1:
                    pass
                elif a == (b-1):
                    aux = arriba.siguiente
                    aux2 = arriba.anterior
                    aux3 = abajo.siguiente
                    aux4 = abajo.anterior
                    arriba.anterior.siguiente = abajo

                    abajo.siguiente.anterior = arriba

                    abajo.anterior = arriba.anterior

                    arriba.siguiente = abajo.siguiente
                    arriba.anterior = abajo
                    abajo.siguiente = arriba
                    auxnum = arriba.id
                    arriba.id = abajo.id
                    abajo.id = auxnum
                    break
                else:
                    pass
                aux = arriba.siguiente
                aux2 = arriba.anterior
                aux3 = abajo.siguiente
                aux4 = abajo.anterior
                
                arriba.siguiente.anterior = abajo
                rrcolumnas = self.eColumnas.primero
                if arriba == self.eColumnas.primero:
                    self.eColumnas.primero = abajo
                    print("ES PRiMERO")
                else:
                    arriba.anterior.siguiente = abajo
                if b == columnas:
                    print("ES ULTIMO")
                    pass
                else:
                    abajo.siguiente.anterior = arriba    
                abajo.anterior.siguiente = arriba

                arriba.siguiente = abajo.siguiente

                arriba.anterior = abajo.anterior

                abajo.siguiente = aux

                abajo.anterior = aux2

                auxnum = arriba.id
                arriba.id = abajo.id
                abajo.id = auxnum  
                a += 1
                b -= 1  

        
        else:
            while a < b:
                arriba = self.eColumnas.getEncabezado(a)
                abajo = self.eColumnas.getEncabezado(b)
                print("ARRIBA ANTES:",arriba.id)
                print("ABAJO ANTES:",abajo.id)
                aux = arriba.siguiente
                aux2 = arriba.anterior
                aux3 = abajo.siguiente
                aux4 = abajo.anterior
                
                arriba.siguiente.anterior = abajo
                rrcolumnas = self.eColumnas.primero
                if arriba == self.eColumnas.primero:
                    self.eColumnas.primero = abajo
                    access = arriba.accesoNodo
                    access2 = abajo.accesoNodo
                    #while access != None:
                        #if access == self.eColumnas.primero.accesoNodo:
                           # self.eColumnas.primero.accesoNodo = access2
                        #rrcolumnas.accesoNodo = access2
                        #au1 = access.abajo
                        #au2 = access2.arriba#

                        #access.abajo.arriba = access2

                        #access2.arriba.abajo = access
                        #access.arriba = au2
                        #access2.abajo = au1
                        #access.abajo = None
                        #access2.arriba = None
                        #auxf = access.fila
                        #access.fila = access2.fila
                        #access2.fila = auxf                        
                        #print("VVVVVVV  COLUMNA:",access.columna, "VVVVVV FILA:",access.fila)
                        #print("BBBBBBB  COLUMNA:",access2.columna, "BBBBBB FILA:",access2.fila)
                        #rrcolumnas = rrcolumnas.siguiente
                        #access = access.derecha
                        #access2 = access2.derecha
                    print("ES PRiMERO")
                else:
                    arriba.anterior.siguiente = abajo
                    #print(arriba.anterior.siguiente.id)    
                if b == columnas:
                    print("ES ULTIMO")
                    pass
                else:
                    abajo.siguiente.anterior = arriba
                abajo.anterior.siguiente = arriba

                arriba.siguiente = abajo.siguiente

                arriba.anterior = abajo.anterior

                abajo.siguiente = aux

                abajo.anterior = aux2

                auxnum = arriba.id
                arriba.id = abajo.id
                abajo.id = auxnum
                access = arriba.accesoNodo
                access2 = abajo.accesoNodo
                a += 1 
                b -= 1   
                print("ARRIBA:",arriba.id)
                print("ABAJO:",abajo.id)
              


            print("ES IMPAR")
    def Transpuesta(self,b):
        eColumna = self.eColumnas.primero
        a = []
        c = []
        print("\n****************************** Recorrido por Columnas ********************")
        while eColumna != None:
            actual = eColumna.accesoNodo      
            x = eColumna.id      
            print("\n Columna "+str(actual.columna))
            print("Fila:  Valor                                    : id")
            x = 0
            while actual != None:
                c.append(actual.valor)
                c.append(actual.fila)
                c.append(actual.columna)
                a.append(c)
                print(str(actual.fila)+"            "+actual.valor+"                   ")
                actual = actual.abajo
                c = []
            b.append(a)
            a = []
            eColumna = eColumna.siguiente

        print("\n****************************** Fin Recorrido por Columnas ********************")
        return b
'''
m = matriz("nombre", 10, 10)
m.insertar(1, 1, "A")
m.insertar(3, 0, "B")
m.insertar(1, 0, "C")
m.insertar(2, 0, "D")
m.insertar(2, 2, "E")
m.insertar(4, 5, "F")
m.insertar(1, 2, "G")

m.recorrerFilas()
m.recorrerColumnas()'''
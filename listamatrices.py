from matriz import matriz
class ListaMatrices:
    def __init__(self):
        self.primero = None

    def insertar(self, nombre, filas, columnas):
        nuevo = matriz(nombre, filas, columnas)
        if self.primero is None:
            self.primero = nuevo
        else:
            temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo 
            nuevo.anterior = temporal

    def mostrardatosf(self):
        temporal = self.primero
        while temporal is not None:
            print("NOMBRE:",temporal.nombre, "FILAS:", temporal.filas, "COLUMNAS:",temporal.columnas)
            print("-----------------DATOS-------------------")
            temporal.recorrerFilas()
            #if(temporal.datos.mostrardatos() != None):
             #   print(temporal.datos.mostrardatos())
            print("-----------------------------------------")
            #while tmp is not None:
             #   print("X:",tmp.datos.)
            temporal = temporal.siguiente

    def getNodoMatriz(self, nombre):
        temporal = self.primero
        while temporal is not None:
            if str.lower(temporal.nombre) == str.lower(nombre):
                return temporal
            temporal = temporal.siguiente
        return None         
from nodos import nodoEncabezado, Nodo


class listaEncabezado:
    def __init__(self, primero= None):
        self.primero = primero


    def setEncabezado(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
        elif nuevo.id < self.primero.id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                if nuevo.id < actual.siguiente.id:
                    nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
            if actual.siguiente == None:
                actual.siguiente = nuevo
                nuevo.anterior = actual        

    def getEncabezado(self,id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente       
        return None        
    
class NodoLista:
    def __init__(self,dato) :
        self.dato = dato 
        self.siguiente = None
        self.anterior = None

class listaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo= None

        

    def insertar(self,datox):
        nuevo=NodoLista(datox)
            
        if (self.primero==None):
            self.primero=self.ultimo=nuevo
        else:
            #self.ultimo.siguiente=nuevo
            nuevo.siguiente = self.primero
            self.primero.anterior= nuevo
            self.primero = nuevo   
        #self.ultimo=nuevo
        self.ultimo.siguiente=self.primero
        self.primero.anterior = self.ultimo

    def imprimir(self):
        print("Elementos de la Lista Doblemente Cirular :")
        aux=self.primero
        while(aux!=None):
            print(aux.dato)
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def buscar(self, busca):
        aux=self.primero
        while(aux!=None):
            if (aux.dato==busca):
                print("Dato Actual ---> ",aux.dato)
                print("Dato Siguiente --->> ",aux.siguiente.dato)
                print("Dato Anterior <<-------",aux.anterior.dato)
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente
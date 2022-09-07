from calendar import c
import csv
from Designacion import Designacion
from NodoLista import NodoLista

class ListaEncadenada:
    __cabeza = None
    
    

    def __init__(self) -> None:
        self.__cabeza = None
        archivo = open("Magistrados.csv")
        reader = csv.reader(archivo,delimiter=",")
        cabecera = False
        for file in reader:
            if cabecera == False:
                cabecera = True
            else:
                NuevaDesignacion = Designacion(file[0],file[1],file[2],file[3],file[4],file[5],file[6])
                NuevoNodo = NodoLista(NuevaDesignacion)
                self.Insertar(NuevoNodo)


        
    
    def Insertar(self,NuevoNodo):
        if self.vacio() :
            NuevoNodo.setSiguiente(self.__cabeza)
            self.__cabeza = NuevoNodo
        else:
            aux = self.__cabeza
           
            while aux.getSiguiente():
                aux = aux.getSiguiente()
            aux.setSiguiente(NuevoNodo)



    def vacio(self):
        return self.__cabeza == None
    
    def Suprimir(self,posicion):
        if self.vacio():
            print("No se puede suprimir lista vacia")
        elif posicion < 0 or posicion >= self.__cantidad+1:
            print("Posicion no valida")
        else:
            aux = self.__cabeza
            actualPos = 1
            while actualPos < posicion-1:
                aux = aux.getSiguiente()
                actualPos += 1
            eliminar = aux.getSiguiente()
            aux.setSiguiente(eliminar.getSiguiente())
            del eliminar
            self.__cantidad -= 1
    
    def puntoC(self,cargo):
        anioActual = self.__cabeza.getValor().getAnio()
        cont = 0
        aux = self.__cabeza
        while aux != None:
            if aux.getValor().getCargo().lower() == cargo.lower():
                if anioActual == aux.getValor().getAnio():
                    cont +=aux.getValor().getMujeres()
                else:
                    print("Anio: {}, Cantidad de mujeres: {}".format(aux.getValor().getAnio(),cont))
                    cont = 0
                    anioActual = aux.getValor().getAnio()
            aux = aux.getSiguiente()

    def puntoD(self,materia,cargo,anio):
        cont = 0
        aux = self.__cabeza
        while aux != None and anio >= aux.getValor().getAnio():
            if aux.getValor().getAnio() == anio and aux.getValor().getMateria().lower() == materia.lower() and aux.getValor().getCargo().lower() == cargo.lower():
                cont += aux.getValor().getMujeres()
                cont += aux.getValor().getVarones()

            aux = aux.getSiguiente()
        
        print("Cantidad de agentes en anio {}, cargo {}, materia {} es de {}".format(anio, cargo.lower(), materia.lower(),cont))
        
    
        
            



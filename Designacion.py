class Designacion:
    __anio = 0
    __justicia = ""
    __cargo = ""
    __instancia = ""
    __materia = ""
    __cant_Varones = 0
    __cant_Mujeres = 0

    def __init__(self,anio,justicia,cargo,instancia,materia,mujeres,varones):
        self.__anio = int(anio)
        self.__justicia =justicia
        self.__cargo = cargo
        self.__instancia = instancia
        self.__materia = materia
        self.__cant_Mujeres = int(mujeres)
        self.__cant_Varones = int(varones)
    
    def getAnio(self):
        return self.__anio
    
    def getJusticia(self):
        return self.__justicia
    
    def getCargo(self):
        return self.__cargo
    
    def getInstancia(self):
        return self.__instancia
    
    def getMateria(self):
        return self.__materia
    
    def getMujeres(self):
        return self.__cant_Mujeres
    
    def getVarones(self):
        return self.__cant_Varones
    
    

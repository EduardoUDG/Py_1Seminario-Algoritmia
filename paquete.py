
class Paquete:
    
    estampilla = "Corazon"
    # Método Constructor __init__
    # Los constructores se llaman init "doble guion bajo"

    def __init__( self ):
        self.__id = "12"# Dos guiones es privado 
        self._origen = "Londres" # Un guion bajo es protected
        self.destino = "Tlajomulco" # Un punto publico
        self.peso = 0.5

    # getters & setters

    def imprimir( self ):
        print( self.estampilla, self.__id )

    def getId( self ):
        return self.__id

    # Protected solo puede ser usada
    # por su misma clase u otras heredaras
    # NO EXISTEN variables protegidas
    # solamente nos ayudan a visualizar esta vairable
    # es protegia y no se debe de tocar mediante p.origen   


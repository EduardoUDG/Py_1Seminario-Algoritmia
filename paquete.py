
class Paquete:

    estampilla = "Corazon"

    def __init__( self,
         id:str, 
         origen:str, 
         destino:str, 
         peso:float ):

        self.__id = id
        self._origen = origen
        self.destino = destino
        self.peso = peso

    # getters & setters

    def imprimir( self ):
        print( "Paquete",self.__id,"va de",self._origen,"a",self.destino,"con un peso de",self.peso,"kg" )

    def getId( self ):
        return self.__id



    # Protected solo puede ser usada
    # por su misma clase u otras heredaras
    # NO EXISTEN variables protegidas
    # solamente nos ayudan a visualizar esta vairable
    # es protegia y no se debe de tocar mediante p.origen   


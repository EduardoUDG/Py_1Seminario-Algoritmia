
from os import fdopen
from paquete import Paquete

# self nos da acceso a nuestra clase

class Paqueteria:
    def __init__(self) -> None:
        self.paquetes = []

    
    def mostrar( self ):
        for e in self.paquetes:
            e.imprimir()

    # usamos self para indicar que trabajaremos 
    # dentro de esta misma clase
    # como paquete es una LISTA tiene varios métodos a usar
    def agregar( self, paquete):
        self.paquetes.append( paquete )
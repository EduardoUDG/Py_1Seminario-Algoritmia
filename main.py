import os
from paquete import Paquete
from paqueteria import Paqueteria

# p = Paquete("12", "Londres", "Tlajomulco", 2.5)

fodex = Paqueteria()

while True:
    os.system("clear")
    print("Selecciona una opcion")
    print("1) Agregar paquete")
    print("2) Mostrar todos los paquetes")
    print("3) Salir")
    opc = int( input("Selecciona una opción: ") )

    if opc == 1:
        id = input("Id: ")
        origen = input("Origen: ")
        destino = input("Destino: ")
        peso = float(input("Peso: "))
    
        fodex.agregar( Paquete(id, origen, destino, peso) )
        input("Paquete agregado correctamente")

    elif opc == 2:
        fodex.mostrar()
        input("\n Presiona ENTER para continuar...")
    elif opc == 3:
        break

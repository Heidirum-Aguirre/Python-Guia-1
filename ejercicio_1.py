import random

azar = random.randint(1, 100)

confirmar = 0

while confirmar == 0:

    numero = int(input("Ingrese un numero para que el codigo lo adivine: "))
    
    if azar < numero:
        print("El numero es Demasiado Alto")
    elif azar > numero:
        print("El numero es Demasiado Bajo")
    else:
        print("Se logro dar con el numero generado!! YEII:D")
        confirmar = 1
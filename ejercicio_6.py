opcion = ""

while opcion != "salir":
    
    palabra = (input("Ingrese la palabra qe desee invertir: "))
    
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra[::-1]
    
    print(f"{palabra}")
    
    opcion = input("En el caso de que desee finalizar el trabajo, escriba (salir), en caso contracio, escriba (seguir): ")
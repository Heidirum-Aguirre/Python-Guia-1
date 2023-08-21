opcion=0

while opcion != 6:
    
    print("¿Que conversion desea realizar?")
    
    print("1) Centimetros -> Pulgadas")
    print("2) Metros -> Kilometros")
    print("3) Onzas -> Gramos")
    print("4) Milla -> Kilometro")
    print("5) Celsius -> Fahrenheit")
    print("6) Salir")
    
    opcion = int(input("Ingrese solo el numero de la opcion: "))
    if opcion == 6:
        break
    conversion = int(input("Indique el numero que desea convertir: "))
    
    if opcion == 1:
        conversion = conversion / 2.54
        
    elif opcion == 2:
        conversion = conversion / 1000
        
    elif opcion == 3:
        conversion = conversion * 28.35
        
    elif opcion == 4:
        conversion = conversion * 1.609
    
    elif opcion == 5:
        conversion = (conversion * (9/5)) + 32
    
    else:
        print("La opcion no esta dentro del rango de opciones")
        
    print(f"El resultado de la conversion elegida es: {conversion}")
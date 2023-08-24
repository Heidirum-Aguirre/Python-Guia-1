while True:
    
    palabra1 = input("Ingrese la primera palabra a rimar: ")
    
    if len(palabra1)>3:
        break
    else:
        print("La palabra no funciona para la rima")

while True:
    palabra2 = input("Ingrese la segunda palabra a rimar: ")
    
    if len(palabra2)>3:
        break
    else:
        print("La palabra no funciona para la rima")

if palabra1[-3]==palabra2[-3]:
    print("Riman")
    
elif palabra1[-2:]==palabra2[-2:]:
    print("Riman un poco")

else:
    print("No riman")
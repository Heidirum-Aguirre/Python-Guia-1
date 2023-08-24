def largo(Lista):
    
    guardar = ""
    
    for a in Lista:
        
        if len(guardar) <= len(a):
            guardar = a
            
    return guardar

    
Lista = []

cantidad = int(input("Ingrese cuantas palabras desee ingresar: "))

    
for b in range(cantidad):
    
    palabra = input("Ingrese una palabra: ")
    
    Lista.append(palabra)
    
resultado = largo(Lista)

print(f"La palabra mas larga de la lista es {resultado}")
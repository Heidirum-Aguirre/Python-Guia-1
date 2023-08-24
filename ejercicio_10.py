lista_compra={}
terminar = ""
coste = 0

while terminar != "terminar":

    articulo = input("Ingrese el articulo de su compra: ")
    precio = int(input("Ingrese el precio del articulo: "))
    
    lista_compra[articulo] = precio
    
    terminar = input(("\nSi desea terminar con la lista de compra ingrese (terminar), en caso de querer seguir colocar (continuar): "))
    
    coste = precio + coste
    
lista_compra["total"] = coste

print("\nLista de la compra:")
for clave, valor in lista_compra.items():
    print(clave ,"=", valor)
    
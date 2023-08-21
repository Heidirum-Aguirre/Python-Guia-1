numero = int(input("Ingrese el numero que desee saber si es primo o no: "))
divisores=0

for a in range(1, numero+1):
    if numero % a == 0:
        divisores=divisores+1
        
if divisores == 2:
    print("Es primo")
else:
    print("No es primo")
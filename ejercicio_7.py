"5! = 5*4*3*2*1"

numero = int(input("Ingrese el numero que desea calcular: "))

factorial = 1

for a in range(1, numero+1):
    factorial = a * factorial
    
print(f"El factorial del numero es: {factorial}")
    
def area(r):
    a = 3.1415 * r**2
    return(a)

def volumen(h,r):
    v= area(r) * h
    return(v)
    
r = int(input("Ingrese el valor del radio del circulo: "))
h = int(input("Ingrese el valor de la altura del cilindro: "))

a=area(r)
v=volumen(h,r)

print(f"El area del circulo es :{a}")
print(f"El volumen del cilindro es :{v}")
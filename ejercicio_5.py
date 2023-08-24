palabra = input("Ingrese una palabra a gusto: ")
letra = input("Eliga la letra que desea contar cuantas veces se repite en su palabra: ")

contador = 0

for letrita in palabra:
    if letrita == letra:
        contador =contador + 1
        
print(f"La letra ({letra}) que usted quiere contar, aparece ({contador}) veces en su palabra ({palabra})")
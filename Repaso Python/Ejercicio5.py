n = int(input("Ingrese la cantidad de invitados: "))
precio = float(input("Ingrese el precio de 1kg de carne: "))

total_carne = n*0.7

total_precio = precio*total_carne

print(f"Deberas comprar un total de {total_carne}kg de carne y vas a gastar ${total_precio}")
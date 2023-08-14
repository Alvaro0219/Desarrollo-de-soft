nombre = input("Ingrese el nombre del socio: ")
edad = int(input("Ingrese la edad del socio: "))

if (edad>=13 and edad<15):
    print(f"{nombre} debe estar en la categoria infantil")
elif(edad>=15 and edad<17):
    print(f"{nombre} debe estar en la categoria cadete")
elif(edad>=17 and edad<19):
    print(f"{nombre} debe estar en la categoria juvenil")
elif(edad>=19):
    print(f"{nombre} debe estar en la categoria mayores")
else:
    print(f"{nombre} no tiene la edad minima para estar en el club")
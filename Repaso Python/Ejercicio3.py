total = float(input("Ingrese el total de la compra: "))

if (total>=3500):
    descuento = total * 0.10
    total = total-descuento
print(f"Usted debera abonar ${total}")

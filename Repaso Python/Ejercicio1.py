"""Promedio de temperaturas
Durante los 5 días de una semana se tomaron mediciones de temperatura en la ciudad. 
Se desea conocer cuál fue la temperatura promedio de la semana. Escriba un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario."""

suma_total = 0

for i in range(5):
    temp = float(input(f"Ingrese la temperatura del dia {i+1}: "))

    suma_total = suma_total+temp

promedio = suma_total/5

print(f"El promedio de lluvias de la semana es: {promedio} °C ")

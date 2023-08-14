"""Funciones para operar sobre una lista
Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:

Muestre la lista
El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores de la lista son mayores a dicho valor, 
para eso debe utilizar una función. La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.
Crear una función que calcule el promedio de la lista y utilizarla.
Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.
"""

from random import randint

lista1 = []

#Cargar datos en la lista
for i in range(10):
    aleatorio = randint(1,20)
    lista1.append(aleatorio)

#Mostrar lista
print(lista1)

def funcion1(lista, nro):
    cont=0

    for i in lista:
        if (i>nro):
            cont+=1
    
    return cont

def funcion2(lista):
    suma=0
    for i in lista:
        suma = suma+i
    
    promedio = suma/10

    return promedio

def funcion3(lista):
    menor=20
    mayor=0
    for i in lista:
        if (i>mayor):
            mayor = i
        if (i<menor):
            menor = i

    return mayor, menor

#FUNCION 1
num = int(input("Ingrese un valor para ver cuantos valores de la lista son mayores al mismo: "))
cant_mayores =funcion1(lista1, num)
print(f"La cantidad de numeros mayores al ingresado son: {cant_mayores}")

#FUNCION 2
promedio = funcion2(lista1)
print(f"El promedio de la lista generada es: {promedio}")

#FUNCION 3
mayor, menor = funcion3(lista1)
print(f"El mayor de la lista es: {mayor}, el menor es: {menor}")



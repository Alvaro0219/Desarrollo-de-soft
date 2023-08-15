from os import system

def ingresar_valor1():
    valor1 = int(input("Ingrese el primer valor: "))

    return valor1

def ingresar_valor2():
    valor2 = int(input("Ingrese el segundo  valor: "))

    return valor2

def suma(v1, v2):
    resultado = v1+v2

    print(f"El resultado de la suma es: {resultado}")

def resta(v1, v2):
    resultado = v1-v2

    print(f"El resultado de la resta es: {v1}")

def multiplicacion(v1,v2):
    resultado = v1*v2

    print(f"El resultado de la multiplicacion es: {resultado}")

def division(v1,v2):
    resultado = v1/0

    print(f"El resultado de la multiplicacion es: {resultado}")


def main ():

    v1= None
    v2 = None

    while True:

        menu = """
            1. Ingresar valor 1
            2. Ingresar valor 2
            3. Mostrar suma
            4. Mostrar resta
            5. Mostrar multiplicación
            6. Mostrar división
            7. Salir

            Ingrese una opcion:  """
        
        opcion = int(input(menu))

        if opcion==1:
            v1 = ingresar_valor1()
        elif opcion==2:
            v2 = ingresar_valor2()
        elif opcion==3:
            if v1 is None or v2 is None:
                print("Error: Debe ingresar ambos valores primero.")
            else:
                system("cls")
                suma(v1,v2)
        elif opcion==4:
            if v1 is None or v2 is None:
                print("Error: Debe ingresar ambos valores primero.")
            else:
                system("cls")
                resta(v1,v2)
        elif opcion==5:
            if v1 is None or v2 is None:
                print("Error: Debe ingresar ambos valores primero.")
            else:
                system("cls")
                multiplicacion(v1,v2)
        elif opcion==6:
            if v1 is None or v2 is None:
                print("Error: Debe ingresar ambos valores primero.")
            else:
                system("cls")
                division(v1,v2)
        elif opcion==7:
            print("Calculadora cerrada")
            break
        else:
            system("cls")
            print("Opcion incorrecta -> Ingrese otra")



if __name__ == '__main__':
    main()
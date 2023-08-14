import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

def imprimir_lista(lista):
	for i in lista:
		print(f"<{i['nombre']}> -: <{i['numero']}> -: (<{i['tiempo_llegada']}>)")
	
def ganador(lista):
    mejor_tiempo = 10000000
    num_atleta = 0
    for i in lista:
        if i['tiempo_llegada'] < mejor_tiempo:
            mejor_tiempo = i['tiempo_llegada']
            num_atleta = i['numero']
            
    return mejor_tiempo, num_atleta

def devolver_datos(numero, lista):
	for i in lista:
		if (i['numero'] == numero):
			print(f"Nombre: {i['nombre']} - Numero: {i['numero']} - Tiempo llegada: {i['tiempo_llegada']}")	
			
def podio(lista):
    num1 = 1000
    num2 = 1000
    num3 = 1000
    for i in lista:
        if i['tiempo_llegada'] < num1:
            num1 = i['tiempo_llegada']
        elif num1 < i['tiempo_llegada'] < num2:
            num2 = i['tiempo_llegada']
        elif num2 < i['tiempo_llegada'] < num3:
            num3 = i['tiempo_llegada']
    
    tupla = (num1, num2, num3)

    return tupla


if __name__ == '__main__':
    atletas = generar_lista_de_atletas()
    imprimir_lista(atletas)
    tiempo, t_ganador = ganador(atletas)
    print(f"El atleta que resulto ganador fue el numero: {t_ganador} con un tiempo de: {tiempo} s")
    num = int(input("Ingrese el numero del competidor que esta buscando: "))
    devolver_datos(num, atletas)
    tupla_podio = podio(atletas)
    print("PODIO DE LLEGADAS EN TIEMPOS")
    print(tupla_podio)
        
	
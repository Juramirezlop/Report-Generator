import msvcrt as m

import matplotlib.pyplot as plt

"""
Generador de reportes de notas
En la mayor parte del programa los parámetros entre funciones se repiten, y ello es porque las funciones se llaman constantemente entre sí y de la misma manera, el intercambio de datos debe ser constante.
"""


def calificaciones(numero_estudiantes, numero_notas, encabezado2, encabezado1):
	"""
	Función encargada de generar la matriz principal que se usará durante la ejecución de todo el código.
	Los ciclos while se crearon con el objetivo de evitar que el programa entrará en un bucle y abortara la operación. Debido a que los datos tratados deben ser de un valor específico si se hace de otra manera el programa abortará
	:param list matriz_cal: Matriz de Notas
	:param string nota: Valor de nota individual
	:param float nota: Valor numérico redondeado de la nota
	:param string nombre: nombre indiviudal de cada estudiante
	:param int a: número iterador del total de estudiantes descritos en la función main(), aquí se agregarán tantos como hayan sido indicados
	:param int b: número iterador del total de notas descritas en la función main(), aquí se agragarán tantas como hayan sido indicadas
	"""
	if encabezado2 == "Notas" or "Total de Notas" or "Compilado de Notas" or "notas" or "total de notas" or "compilado de notas":
		encabezado2 = "Nota"

	matriz_cal = []
	
	for a in range(numero_estudiantes):
		matriz_cal.append([])
		for b in range(numero_notas+1):
			if b == 0:
				nombre = input("{} {}: ".format(encabezado1, a+1))
				while len(nombre) == 0:
					nombre = input("Ingrese un(a) {} {} Válido: ".format(encabezado1, a+1))
				while 48 <= ord(nombre[0]) and 57 >= ord(nombre[0]):
					nombre = input("Ingrese un(a) {} {} Válido: ".format(encabezado1, a+1))
					while len(nombre) == 0:
						nombre = input("Ingrese un(a) {} {} Válido: ".format(encabezado1, a+1))
				matriz_cal[a].append(nombre)
			else:
				nota = input("{}, {} {}: ".format(nombre, encabezado2, b))
				while len(nota) == 0:
					nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, encabezado2, b))
					if len(nota) == 0:
						continue
					else:
						while 48 > ord(nota[0]) and 57 < ord(nota[0]):
							nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, encabezado2, b))
							if len(nota) == 0:
								break
				while 48 > ord(nota[0]) or 57 < ord(nota[0]):
					nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, encabezado2, b))
					while len(nota) == 0:
						nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, encabezado2, b))
					
				nota = round(float(nota), 2)
					
				matriz_cal[a].append(nota)

	print()
	print("Presione Cualquier Tecla Para Continuar...")
	wait()

	menu_de_seleccion(matriz_cal, encabezado1, encabezado2, numero_estudiantes, numero_notas)


def notas(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):
	
	"""
	Función encargade de imprimir la tabla de notas actual con los datos presentes.
	:param int contador: variable encargada de indicar en el f-string el nombre del estudiante al cual las notas consecuntes perteneces
	:param list fila[]: itera entre las distintas sublistas presnentes en la matriz principal matriz_cal, para imprimir de manera individual sus valores al usuario en una misma fila
	:param obj elemento: encargado de iterar en todos los datos dentro de las sublistas definidas por fila para su posterior impresión con el uso de f-string
	:param function wait(): espera interacción del usuario para continuar antes de volver al menu principal denomidado menu_de_seleccion
	:param function encabezado(): sólo imprime el encabezado de la tabla en pantalla con los criterios dados al inicio del programa
	"""
	encabezado(parte1, parte2)
	
	contador = 0

	for fila in matriz_cal:
		contador += 1
		for elemento in fila: 
			if type(elemento) == str:
				print(f"|{contador:<3} {elemento:<36}", end="")
			else:
				print(f"|{elemento:<4}", end="|")
		print()
	print("Presione Cualquier Tecla para Continuar")
	wait()
	wait()
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)


def modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):
	"""
	Función dispuesta para la mdodificación de datos respecto a los ya ingresados. Funciona con sentencias print() para guiar al usuario a un punto específico del programa.
	Los ciclos while se crearon con el objetivo de evitar que el programa entrará en un bucle y abortara la operación. Debido a que los datos tratados deben ser de un valor específico si se hace de otra manera el programa abortará
	Tiene un menu de selecció que permite al usuarion acceder a las distintas opciones de modificación de datos
	:param string e int seleccion: es la vaiable de entrada que después de traducida a entera le permite al progrma reconocer hacía dónde llevar al usuario para proceder. Posteriormente se convierte para indicar el número de estudiante a referir.
	:param string yes: indicador de confirmación para proceder con la ejecución del programa acorde a las instrucciones del usuario; tiene ciclose while inmersos para evitar que la ejecución del programa aboratara al recibir datos inválidos.
	:param string e int seleccion2: permite la navegación del usuario entre el menud de cambio sin alterar otras variables. Su valor final es entero y cualquier otro tipo será detectado como inválido.
	:param string o int seleccion1: permite la selección del tipo de modicfiación que se desea usar sin alterar otras variables. Es un seleccionador secundario.
	:param function wait(): espera interacción del usuario para continuar con la ejecución del código.
	:param function modulo_de_cambio: función definida para realizar cambios a los datos actuales.
	:param function menu_de_seleccion: menu anterior para navegar en opciones distintas a la de modificación.
	:param function notas_copia: permite visualizar los datos actuales sin necesidad de entrar a menús distintos.
	"""
	print()
	print("Este módulo es para modificar la información por estudiante")
	print()
	print("Presione Cualquier Tecla para Continuar")
	print()
	wait()
	seleccion = input(("Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ")).upper()
	
	while len(seleccion) == 0:
		seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()
		if len(seleccion) == 0:
			continue
		else:
			while seleccion != "N" and seleccion != "T" and (48 > ord(seleccion[0]) or 57 < ord(seleccion[0])):
				seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()
				if len(seleccion) == 0:
					break
	while seleccion != "N" and seleccion != "T" and (48 > ord(seleccion[0]) or 57 < ord(seleccion[0])):
		seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()
		while len(seleccion) == 0:
			seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()

	print("{}, ¿es esto correcto?".format(seleccion))
	
	yes = input("(S/N): ").upper()
	
	while yes != "N" and yes != "S":
			yes = input("(S/N): ").upper()
	
	while yes == "N":
		seleccion = input(("Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ")).upper()
	
		while len(seleccion) == 0:
			seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()
			if len(seleccion) == 0:
				continue
			else:
				while seleccion != "N" and seleccion != "T" and (48 > ord(seleccion[0]) or 57 < ord(seleccion[0])):
					seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()
					if len(seleccion) == 0:
						break
		while seleccion != "N" and seleccion != "T" and (48 > ord(seleccion[0]) or 57 < ord(seleccion[0])):
			seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()
			while len(seleccion) == 0:
				seleccion = input('Ingrese número de estudiante a modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()

		print("{}, ¿es esto correcto?".format(seleccion))
		yes = input("(S/N): ").upper()
		if yes == "S":
			continue
	
	if seleccion == "N":
		
		menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
	elif seleccion == "T":
		notas_copia(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
	else: 

		while int(seleccion) > len(matriz_cal) and seleccion != "0":
			seleccion = input("Seleccione Número de Estudiante Existente: ")
			while len(seleccion) == 0:
				seleccion = input("Seleccione Número de Estudiante Existente: ")
			while ord(seleccion[0]) < 48 and ord(seleccion[0]) > 57:
				seleccion = input("Seleccione Número de Estudiante Existente: ")
				while len(seleccion) == 0:
					seleccion = input("Seleccione Número de Estudiante Existente: ")

		seleccion = int(seleccion)-1

		
		print("El número {}, pertenece al estudiante {},". format(seleccion+1, matriz_cal[seleccion][0]), "¿está seguro que desea continuar?")
		yes = input("(S/N): ").upper()

	
		while yes != "N" and yes != "S":
			yes = input("(S/N): ").upper()

		if yes == "N":
			while yes == "N": 
				modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
		else: 
			print("                                OPCIONES DE CAMBIO")
			print()
			print("                               ====================")
			print()
			print("                0. Agregar Estudiantes y Notas o Cambiar Datos")
			print()
			print("                1. Agregar o Borrar Notas a Estudiante")
			print()
			print("                2. Consultar Notas por Estudiante")
			print()
			print("                3. Salir")
			print()

			seleccion2 = input("Por favor seleccione una opción: ")

			while len(str(seleccion2)) == 0:
				seleccion2 = input("Por favor seleccione una opción: ")
				

			while seleccion2 != '0' and seleccion2 != '1' and seleccion2 != '2' and seleccion2 != '3':
				seleccion2 = input("Por favor seleccione una opción: ")
				while len(seleccion2) == 0:
					break
				yes = input(f"{seleccion2}, ¿Es esto Correcto?, (S/N): ").upper()
	
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()

				while yes == "N":
					if yes == "N": 
						seleccion2 = input("Por favor seleccione una opción: ")
						yes = input(f"{seleccion2}, ¿Es esto Correcto?, (S/N): ").upper()
						while yes != "N" and yes != "S":
							yes = input("(S/N): ").upper()
					else:
						break

			seleccion2 = int(seleccion2)

			if seleccion2 == 0:

				modulo_cambio(matriz_cal, parte1, parte2,  numero_estudiantes, numero_notas)

			if seleccion2 == 1:

				seleccion1 = input("Por Favor Seleccione una Opción para Continuar, S para agregar notas o B para borrar: ").upper()
				print(seleccion1)

				while len(seleccion1) == 0:
					seleccion1 = input("Por Favor Seleccione una Opción para Continuar, S para agregar notas o B para borrar: ").upper()
				while seleccion1 != "S" and seleccion1 != "B":
						seleccion1 = input("Por Favor Seleccione una Opción para Continuar, S para agregar notas o B para borrar: ").upper()
						while len(seleccion1) == 0:
							seleccion1 = input("Por Favor Seleccione una Opción para Continuar, S para agregar notas o B para borrar: ").upper()

				if seleccion1 == "S": 

					seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Adicionar: ")
				
					while len(seleccion2) == 0:
						seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Adicionar: ")
					while 48 > ord(seleccion2[0]) or 57 < ord(seleccion2[0]):
							seleccion2 = input("Por Favor Ingrese Número Adicional de Notas")
							while len(nota) == 0:
								seleccion2 = input("Por Favor Ingrese Número Adicional de Notas")

					seleccion2 = int(seleccion2)
					seleccion = int(seleccion)

					for b in range(1,seleccion2+1):
						nota = input("{}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b))
						while len(nota) == 0:
							nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal[seleccion])+b))
							if len(nota) == 0:
								continue
							else:
								while 48 > ord(nota[0]) and 57 < ord(nota[0]):
									nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal[seleccion])+b))
									if len(nota) == 0:
										break
						while 48 > ord(nota[0]) and 57 < ord(nota[0]):
							nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal[seleccion])+b))
							while len(nota) == 0:
								nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal[seleccion])+b))
							
					
						nota = round(float(nota), 2)
					
						matriz_cal[seleccion].append(nota)

					print("Tarea realizada con éxtio, presione cualquier tecla para continuar: ")
					wait()
					modificar(matriz_cal, parte1, parte2,  numero_estudiantes, numero_notas)

				if seleccion1 == "B": 
						
					seleccion2 = input("Por Favor Ingrese Código de Nota a Borrar: ")
				
					while len(seleccion2) == 0:
						seleccion2 = input("Por Favor Ingrese Código de Nota a Borrar: ")
					while 48 > ord(seleccion2[0]) or 57 < ord(seleccion2[0]):
							seleccion2 = input("Por Favor Ingrese Código de Nota a Borrar: ")
							while len(seleccion2) == 0:
								seleccion2 = input("Por Favor Ingrese Código de Nota a Borrar: ")

					seleccion2 = int(seleccion2)
					seleccion = int(seleccion)
					
					del(matriz_cal[seleccion][seleccion2])

					print("Tarea realizada con éxtio, presione cualquier tecla para continuar: ")
					wait()
					modificar(matriz_cal, parte1, parte2,  numero_estudiantes, numero_notas)
			
			if seleccion2 == 2:

				notas_copia(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)

			if seleccion2 == 3:

				menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)


def notas_copia(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):
	"""
	Copia de la función notas para uso específico de la función modifiar, se creo independiente debido a los problemas asociados a usar la misma función para ambos casos pues la originial volvía a menu_de_seleccion().
	:param int contador: variable encargada de indicar en el f-string el nombre del estudiante al cual las notas consecuntes perteneces
	:param sublist fila: itera entre las distintas sublistas presnentes en la matriz principal matriz_cal, para imprimir de manera individual sus valores al usuario en una misma fila
	:param obj elemento: encargado de iterar en todos los datos dentro de las sublistas definidas por fila para su posterior impresión con el uso de f-string
	:param function wait(): espera interacción del usuario para continuar antes de volver a función invocadora modificar()
	:param function encabezado(): sólo imprime el encabezado de la tabla en pantalla con los criterios dados al inicio del programa
	"""
	encabezado(parte1, parte2)
	
	contador = 0

	for fila in matriz_cal:
		contador += 1
		for elemento in fila: 
			if type(elemento) == str:
				print(f"|{contador:<3} {elemento:<36}", end="")
			else:
				print(f"|{elemento:<4}", end="|")
		print()
	print("Presione Cualquier Tecla para Continuar: ")
	wait()
	wait()
	modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
				

def modulo_cambio(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):

	"""
	Funcion para cambiar o agregar datos a la matriz principal.
	Los ciclos while se crearon con el objetivo de evitar que el programa entrará en un bucle y abortara la operación. Debido a que los datos tratados deben ser de un valor específico si se hace de otra manera el programa abortará
	:param string o int seleccion: seleccion de opciones del menú principal y en menús posteriores indicador del índice por estudiante a revisar. Si la opción especificada no se encuentra, se volverá a preguntar.
	:param string e int numero_estudiantes1: nuevo número de estudiantes que se agregan como nuevos datos. 
	:param string e int numero_notas1: nuevo núermo de notas a agregar por estudiante nuevo. 
	:param int a: iterador de los datos en la matriz original para agregar los nuevos datos en el a indicado.
	:param int b: iterador de los nuevos valores de entrada para las notas de los nuevos estudiantes.
	:param string and int seleccion2: seleccionador del menu de modificacion, si el parámetro no es válido dentro de las opciones del menú el programa volverá a preguntar.
	:param string e int nota: indicador de notas adicionales por estudiante; si el carácter es unválido el programa volverá a preguntar..
	:param string nombre: nombre del estudiante nuevo a ser agregadao; si el parámetro es inválido el programa volverá a preguntar.
	:param function modificar(): regreso a menún principal defincición de modificación.
	:param function wait(): espera hasta la interaccíón del usuario para continuar.
	:param list matriz_cal[]: lista principal contenedora de los datos del estudiante.
	"""
	
	seleccion = input("Seleccione una opción; agregar nuevos datos, S, para modificar datos, M: ").upper()

	while seleccion != "S" and seleccion != "M":
			seleccion = input("Seleccione una opción; agregar nuevos datos, S, para modificar datos, M: ").upper()

	if seleccion == "S":

		numero_estudiantes1 = input("Por Favor Indique Cuántos Estudiantes se Van a Agregar: ")
		while len(numero_estudiantes1) == 0:
			numero_estudiantes1 = input("Por Favor Indique Cuántos Estudiantes se Van a Agregar: ")
		while 48 > ord(numero_estudiantes1[0]) > 57:
			numero_estudiantes1 = input("Por Favor Indique Cuántos Estudiantes se Van a Agregar: ")
			while len(numero_estudiantes1) == 0:
				numero_estudiantes1 = input("Por Favor Indique Cuántos Estudiantes se Van a Agregar: ")

		numero_estudiantes1 = int(numero_estudiantes1)

		numero_notas1 = input("Por Favor Indique Cuántas Notas por Estudiante Nuevo se van a Agregar: ")
		while len(numero_notas1) == 0:
			numero_notas1 = input("Por Favor Indique Cuántas Notas por Estudiante Nuevo se van a Agregar: ")
		while 48 > ord(numero_notas1[0]) > 57:
			numero_notas1 = input("Por Favor Indique Cuántas Notas por Estudiante Nuevo se van a Agregar: ")
			while len(numero_notas1) == 0:
				numero_notas1 = input("Por Favor Indique Cuántas Notas por Estudiante Nuevo se van a Agregar: ")

		numero_notas1 = int(numero_notas1)

		for a in range(numero_estudiantes, numero_estudiantes1+1):
			matriz_cal.append([])
			for b in range(numero_notas1+1):
				if b == 0:
					nombre = input("{} {}: ".format(parte1, a+1))
					while len(nombre) == 0:
						nombre = input("Ingrese un(a) {} {} Válido: ".format(parte1, a+1))
					while 48 <= ord(nombre[0]) and 57 >= ord(nombre[0]):
						nombre = input("Ingrese un(a) {} {} Válido: ".format(parte1, a+1))
						while len(nombre) == 0:
							nombre = input("Ingrese un(a) {} {} Válido: ".format(parte1, a+1))
					matriz_cal[a].append(nombre)
				else:
					nota = input("{}, {} {}: ".format(nombre, parte2, b))
					while len(nota) == 0:
						nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, parte2, b))
						if len(nota) == 0:
							continue
						else:
							while 48 > ord(nota[0]) and 57 < ord(nota[0]):
								nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, parte2, b))
								if len(nota) == 0:
									break
					while 48 > ord(nota[0]) or 57 < ord(nota[0]):
						nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, parte2, b))
						while len(nota) == 0:
							nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, parte2, b))
					
					nota = round(float(nota), 2)
					
					matriz_cal[a].append(nota)

					print("Presione Cualquier Tecla Para Continuar...")
					wait()

		modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)

	elif seleccion == "M":

		seleccion = input("Por Favor Seleccione el Código de Estudiante a ser Modificado: ")

		while len(seleccion) == 0:
			seleccion = input("Por Favor Seleccione el Código de Estudiante a ser Modificado: ")
			while ord(seleccion[0]) > 57 and ord(seleccion[0]) < 48:
				seleccion = input("Por Favor Seleccione el Código de Estudiante a ser Modificado: ")
				if len(seleccion) == 0:
					break

		while int(seleccion) > len(matriz_cal) and seleccion != "0":
			seleccion = input("Seleccione Número de Estudiante Existente: ")
			while len(seleccion) == 0:
				seleccion = input("Seleccione Número de Estudiante Existente: ")
			while ord(seleccion[0]) < 48 and ord(seleccion[0]) > 57:
				seleccion = input("Seleccione Número de Estudiante Existente: ")
				while len(seleccion) == 0:
					seleccion = input("Seleccione Número de Estudiante Existente: ")

		seleccion = int(seleccion)-1
	

		seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Modificar, E, para hacerlo por código de nota o N para cambiar el nombre: ").upper()
				
		while len(seleccion2) == 0:
			seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Modificar, E, para hacerlo por código de nota o N para cambiar el nombre: ").upper()
		while 48 > ord(seleccion2[0]) and 57 < ord(seleccion2[0]) and seleccion2 != "E":
				seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Modificar, E, para hacerlo por código de nota o N para cambiar el nombre: ").upper()
				while len(nota) == 0:
					seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Modificar, E, para hacerlo por código de nota o N para cambiar el nombre: ").upper()
					 
		if seleccion2 == "E":

			seleccion2 = input("Ingrese el Código de Nota a ser Modificado: ")

			while len(seleccion2) == 0:
				seleccion2 = input("Ingrese el Código de Nota a ser Modificado: ")
				while ord(seleccion2[0]) > 48 and ord(seleccion2[0]) > 57:
					seleccion2 = input("Ingrese el Código de Nota a ser Modificado: ")
			while ord(seleccion2[0]) > 48 and ord(seleccion2[0]) > 57:
				seleccion2 = input("Ingrese el Código de Nota a ser Modificado: ")
				if len(seleccion2) == 0:
					seleccion2 = input("Ingrese el Código de Nota a ser Modificado: ")

			seleccion2 = int(seleccion2)

			
			nota = input("{}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+seleccion2-1))
			while len(nota) == 0:
				nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b-1))
				if len(nota) == 0:
					continue
				else:
					while 48 > ord(nota[0]) and 57 < ord(nota[0]):
						nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b-1))
						if len(nota) == 0:
							break
			while 48 > ord(nota[0]) and 57 < ord(nota[0]):
				nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b-1))
				while len(nota) == 0:
					nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b-1))
							
			nota = round(float(nota), 2)
					
			matriz_cal[seleccion][seleccion2] = nota
			print()
			print("Presione Cualquier Tecla Para Continuar...")
			wait()


		elif seleccion2 == "N":

			
			nombre = input("Ingrese nuevo {}, {}: ".format( parte1, matriz_cal[seleccion][0]))

			matriz_cal[seleccion][0] = nombre
			print()
			print("Presione Cualquier Tecla Para Continuar...")
			wait()

			modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)



		else: 
			seleccion2 = int(seleccion2)

			for b in range(seleccion2-1, seleccion2):
				nota = input("{}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b-1))
				while len(nota) == 0:
					nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b))
					if len(nota) == 0:
						continue
					else:
						while 48 > ord(nota[0]) and 57 < ord(nota[0]):
							nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b))
							if len(nota) == 0:
								break
				while 48 > ord(nota[0]) and 57 < ord(nota[0]):
					nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b))
					while len(nota) == 0:
						nota = input("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b))
							
			nota = round(float(nota), 2)
					
			matriz_cal[seleccion][seleccion2] = nota
			print()
			print("Presione Cualquier Tecla Para Continuar...")
			wait()

		modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)


def final(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):

	"""
	Se encarga de mostrar la nota deifinitiva para el periodod de timepo especificado acorde a la totalidad de notas. Cada nota tiene el mismo peso, no se puede realizar sobre procentajes.
	:param string parte3: cambio del valor de la tabla del encabezado para desglosar el texto especidicado.
	:param function encabezado(): función que imprime el encabezado de la tabla.
	:param int contador: iterador para el f-string 
	:param int contador1: acumula valores a ser divididos para la obtención de la nota final
	:param int suma: valor final de la calificación.
	:param function wait(): espera una respuesta del usuario para continuar con la ejecución del código.
	:param function menu_de_seleccion(): regresa al menu de opción del reporte.
	"""


	parte3 = "Notas Finales (ponderado)"

	encabezado(parte1, parte3)

	contador = 0
	contador1 = 0
	suma = 0

	for fila in matriz_cal:
		contador += 1
		suma = 0
		contador1 = 0
		for elemento in fila: 
			if type(elemento) == str:
				print(f"|{contador:<3} {elemento:<36}", end="")
			else:
				suma = suma + elemento
				contador1 += 1

		suma = round((suma)/(contador1), 2)
		print(f"|{suma:<4}", end="|")
		print()
	
	print("Presione Cualquier Tecla para Continuar: ")
	wait()
	wait()
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)


def menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):
	"""
	Menú de selección principal para las opcionesd el reporte. 
	Los ciclos while se crearon con el objetivo de evitar que el programa entrará en un bucle y abortara la operación. Debido a que los datos tratados deben ser de un valor específico si se hace de otra manera el programa abortará
	:param string e int seleccion: indicador de una opción dentro del menú, si es inválida el programa volverá a preguntar.
	:param string yes: variable de confirmación de selección opción menú; si el caracter es inválido el programa volverá a preguntar.
	:param function notas(): función para la consulta de la información presente en la matriz principal matriz_cal[].
	:param funcition final(): función para la generación de notas finales sobre los datos presentes en la matriz principal.
	:param funcition tabla(): generador de la tabla de rendimiento individual del estudiante.
	:param function diagrama(): generación de un diagrama de barras general con las notas definitivas por estudiante.
	:param function modificar(): acceso a datos para su modificación. 
	"""
	print("                                OPCIONES DE REPORTE")
	print()
	print("                                ===================")
	print()
	print("                0. Generar Resultado Final por Estudiante")
	print()
	print("                1. Generar Tabla Rendimiento por Estudiante")
	print()
	print("                2. Consultar Notas por Estudiante")
	print()
	print("                3. Generar Diagrama con Rendimiento Ponderado General")
	print()
	print("                4. Modificar Datos")
	print()
	print("                5. Salir")
	print()

	seleccion = input("Seleccione una Opción: ")

	while seleccion != '0' and seleccion!= '1' and seleccion != '2' and seleccion != "3" and seleccion != "4" and seleccion != "5":
		seleccion = input("Seleccione una Opción: ")
	
		
	print(str(seleccion) + ", ¿es esta opción correcta?")
	
	
	yes = input("(S/N): ").upper()
	
	while yes != "S" and yes != "N":
		yes = input("(S/N): ").upper()

	if yes == "S":
			
		if seleccion == "2":
			notas(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
		elif seleccion == "0":
			final(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
		elif seleccion == "1":
			tabla(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
		elif seleccion == "3":
			diagrama(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
		elif seleccion == "4":
			modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)
		else:
			exit()
	
	elif yes == "N":
		menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)

def tabla(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):
	"""
	Imprime un gráfico del comportamiento del nivel académico del alumno, es uno individual.
	:param str e int seleccion: indicador del código de estudiante a ser revisado para la generación de la tabla.
	:param list matriz_secundaria[]: copia específica de los datos del estudiante presentes en la matriz original.
	:param list matriz_terciaria[int]: lista de indicadores de las notas.
	:param maltloplib fig, axs: generador de la ventana contenedora de la tabla.
	:param maltloplib axs.plot: gráfico de las listas.
	:param function wait(): espera interacción del usuario para continuar la ejecución del código.
	:param function menu_de_seleccion(): vuelta al menu principal.
	"""

	seleccion = input("Por Favor Ingrese Código Estudiante a Revisar: ")
	
	while len(seleccion) == 0:
		seleccion = input("Por Favor Ingrese Código Estudiante a Revisar: ")

	while ord(seleccion[0]) < 48 or ord(seleccion[0]) > 57 or int(seleccion) > len(matriz_cal):
		seleccion = input("Por Favor Ingrese Código Estudiante a Revisar: ")
		while len(seleccion) == 0:
			seleccion = input("Por Favor Ingrese Código Estudiante a Revisar: ")

	seleccion = int(seleccion)-1

	matriz_secundaria = matriz_cal[seleccion]

	matriz_terciaria = [0]
	
	contador = 0
	for elemento in matriz_secundaria[1:]:
		contador += 1
		matriz_terciaria.append(contador)

	matriz_alv = [0]

	for elemento in matriz_secundaria[1:]:
		matriz_alv.append(elemento)
	

	fig, axs = plt.subplots(1, 1)
	if len(matriz_cal[seleccion]) < 2:
		axs.plot(matriz_terciaria[1:], matriz_alv[1:], 'o', color = 'red', label= 'Rendimiento {}'.format(matriz_secundaria[0]))
	else:
		axs.plot(matriz_terciaria[1:], matriz_alv[1:], color = 'red', label= 'Rendimiento {}'.format(matriz_secundaria[0]))
	plt.title(f'Rendimiento {matriz_secundaria[0]}')
	plt.ylabel("Nota Obtenida")
	plt.xlabel("Número Nota")
	plt.legend()
	plt.show()
	plt.grid()



	input("Presione Cualquier Tecla para Continuar...")

	wait()
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)


def diagrama(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas):

	"""
	Generador del diagrama con los resultados de las notas ponderadas a nivel general; todos los estudiantes.
	:param int contador1: acumula las notas por estudiante
	:param int suma: ponderado de las notas presentes
	:param list matriz_cal_final[float]: lista de los ponderados por estudiante
	:param list matriz_terciaria[str]: lista de nombres de los estudiantes
	:param maltloplib fig, as: ventana con la impresion de los datos.
	:param function wait(): espera interaccion de usuario para seguir con la ejecución del código.
	:param function menu_de_seleccion: menu anterior de opciones
	"""

	contador1 = 0
	suma = 0

	matriz_cal_final = []
	matriz_terciaria = []

	for i in range(len(matriz_cal)):

		suma = 0
		contador1 = 0
		for elemento in matriz_cal[i]:
			if type(elemento) == str:
				matriz_terciaria.append(elemento)
			else:
				suma = suma + elemento
				contador1 += 1

		suma = round((suma)/(contador1), 2)

		matriz_cal_final.append(suma)
	
	names = matriz_terciaria[:]
	values = matriz_cal_final[:]

	fig, ax = plt.subplots()
	ax.bar(names, values, color='gray', width = 0.5)
	fig.suptitle('Rendimiento General')
	ax.legend()
	ax.grid()
	plt.ylabel("Nota Final")
	plt.xlabel("Nombre Estudiante")
	plt.show()

	input("Presione Cualquier Tecla para Continuar...")

	wait()
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas)

def encabezado(Parte1, Parte2):
	"""
	Función encarga de imprimir el cabezado de la tabla para las funciones notas() y notas_copia().
	:param string Parte1: indicador del criterio 1 para la tabla de notas; originalmente definido como Notas. La sangría dada por el f-string es la misma que en las funciones mencionadas.
	:param string Parte2: indicador del croterio 2 para la tabla de notas; originalmente definido como Nombre La sangría dada por el f-string es la misma que en las funciones mencionadas.
	:param string numeral: separador para indicar el código del estudiante, su nivel de sangría coincide con el de las funciones ya mencionadas.
	"""
	numeral = "#"
	print(f"|{numeral:<3} {Parte1:<36}|{Parte2:<}", end="")
	print()


def wait():
	"""
	Espera interacción del usuario para seguir con la ejecución del programa. 
	:param library m: librería que permite el uso de códigos propios del lenguaje C para su ejecución en Python.
	"""
	m.getch()


def main1():
	"""
	Primera interfaz del programa para la creación del nuevo repote. 
	Los ciclos while se crearon con el objetivo de evitar que el programa entrará en un bucle y abortara la operación. Debido a que los datos tratados deben ser de un valor específico si se hace de otra manera el programa abortará
	:param string e int selecccion: opción de selección de menú, si al convertir la variabla a entero, esta no existe en el menú, el programa volverá a preguntar.
	:param string e int numero_estudiantes: numero total de estudiantes tenidos en cuenta para la ejecución del código y creación de los datos; si al converir no se encuentra un entero válido el programa volverá a preguntar. 
	:param string e int numero_noreas: numero totoal de notas a tener en cuenta por estudiante.
	:param string Parte1: criterio 1 de la tabla, definido por defecto como Notas. Sino se encuentra un carácter válido el programa volverá a preguntar.
	:param string Parte2: criterio 2 de la tabla, definido por defecto como Nombre. Sino se encuentra un carácter válido el programa volverá a preguntar.
	:param function calificactiones(): funcion para la creación de la matriz de las notas.
	:param function main1(): reinicio de la función main.

	"""
	print("                  REPORTE DE NOTAS")
	print()
	print("                 ===================")
	print()
	print("                 Bienvenido al reporte de notas.")
	print()
	print("                 1. Nuevo Reporte")
	print()
	print("                 2. Volver al Menu anterior")
	print()
	
	print("Seleccione una opción para continuar: ", end = "")
	seleccion = input()
	

	while seleccion != "1" and seleccion != "2":
		print("Seleccione una opción válida: ", end="")
		seleccion = input()

	print(str(seleccion) + ", ¿es esta opción correcta?")
	yes = input("(S/N): ").upper()

	while yes != "S" and yes != "N":
		yes = input("(S/N): ").upper()
	
	if yes == "S":

		if seleccion == "2":
			exit()

		else:
			print("Para iniciar, por favor presione cualquier tecla...")
			wait()
			print()

			numero_estudiantes = input('Ingrese Cantidad de Estudiantes: ')
			while len(numero_estudiantes) == 0:
				numero_estudiantes = input('Ingrese Cantidad Válida de Estudiantes: ')
			
			while (48 > ord(numero_estudiantes[0]) or 57 < ord(numero_estudiantes[0])): 
				while len(numero_estudiantes) > 1:
					break
				numero_estudiantes = input('Ingrese Cantidad Válida de Estudiantes: ')
				while len(numero_estudiantes) == 0:
					numero_estudiantes = input('Ingrese Cantidad Válida de Estudiantes: ')
						
			numero_estudiantes = int(numero_estudiantes)
			print()
			print("{}, ¿es esto correcto?".format(numero_estudiantes))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
			while yes == "N":
				numero_estudiantes = input('Ingrese Cantidad de Estudiantes: ')
				while len(numero_estudiantes) == 0:
					numero_estudiantes = input('Ingrese Cantidad Válida de Estudiantes: ')
					
				while (48 > ord(numero_estudiantes[0]) or 57 < ord(numero_estudiantes[0])):
					while len(numero_estudiantes) > 1 and (48 > ord(numero_estudiantes[0]) or 57 < ord(numero_estudiantes[0])):
						break
					numero_estudiantes = input('Ingrese Cantidad Válida de Estudiantes: ')
					while len(numero_estudiantes) == 0:
						numero_estudiantes = input('Ingrese Cantidad Válida de Estudiantes: ')
						

				numero_estudiantes = int(numero_estudiantes)
				print("{}, ¿es esto correcto?".format(numero_estudiantes))
				yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			
				
			numero_notas = input('Ingrese Total de Notas: ')
			
			
			while len(numero_notas) == 0:
				numero_notas = input('Ingrese Total Válido de Notas: ')

			while (48 > ord(numero_notas[0]) or 57 < ord(numero_notas[0])):
				while len(numero_notas) > 1 and (48 > ord(numero_notas[1]) or 57 < ord(numero_notas[1])):
					break
				numero_notas = input('Ingrese Total Válido de Notas: ')
				while len(numero_notas) == 0:
					numero_notas = input('Ingrese Total Válido de Notas: ')

			numero_notas = int(numero_notas)
			print()
			print("{}, ¿es esto correcto?".format(numero_notas))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
			while yes == "N":
				numero_notas = input('Ingrese Total de Notas: ')
				while len(numero_notas) == 0:
					numero_notas = input('Ingrese Total Válido de Notas: ')

				while (48 > ord(numero_notas[0]) or 57 < ord(numero_notas[0])) or len(numero_notas) > 1 and (48 > ord(numero_notas[1]) or 57 < ord(numero_notas[1])):
					numero_notas = input('Ingrese Total Válido de Notas: ')
					while len(numero_notas) == 0:
						numero_notas = input('Ingrese Total Válido de Notas: ')
						
				numero_notas = int(numero_notas)
				print("{}, ¿es esto correcto?".format(numero_notas))
				yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			Parte1= input("Por Favor Ingrese Criterio de tabla 1 (Notas): ")

			while len(Parte1) == 0 or (48 <= ord(Parte1[0]) and ord(Parte1[0]) <= 57):
				Parte1 = input('Por Favor Ingrese Criterio tabla 1 Válido (Notas): ')

			print("{}, ¿es esto correcto?".format(Parte1))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
			while yes == "N":
				Parte1= input("Por Favor Ingrese Criterio tabla 1 (Notas): ")

				while len(Parte1) == 0 or (48 <= ord(Parte1[0]) and ord(Parte1[0]) <= 57):
					Parte1 = input('Por Favor Ingrese Criterio tabla 1 Válido (Notas): ')

				print("{}, ¿es esto correcto?".format(Parte1))
				yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			print()
			Parte2 = input("Por Favor Ingrese Criterio tabla 2 (Nombre, etc): ")

			while len(Parte2) == 0 or (48 <= ord(Parte2[0]) and ord(Parte2[0]) <= 57):
				Parte2 = input('Por Favor Ingrese Criterio tabla 2 Válida (Nombre, etc): ')

			print("{}, ¿es esto correcto?".format(Parte2))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
				yes = input("(S/N): ").upper()
			while yes == "N":
				Parte2= input("Por Favor Ingrese Criterio tabla 2 (Nombre, etc): ")

				while len(Parte2) == 0 or (48 <= ord(Parte2[0]) and ord(Parte2[0]) <= 57):
					Parte2 = input('Por Favor Ingrese Criterio tabla 2 Válida (Nombre, etc): ')

				print("{}, ¿es esto correcto?".format(Parte2))
				yes = input("(S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			print()
			calificaciones(numero_estudiantes, numero_notas, Parte1, Parte2)
	if yes == "N":
		main1()

def exit():
	"""
	Función de salida del programa para terminar con la ejecución del código
	"""
	print("Presione Cualquier Tecla para Continuar")
	wait()

main1()
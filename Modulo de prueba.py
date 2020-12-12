import msvcrt as m

import matplotlib.pyplot as plt

diccionario = {}

"""
Generador de reportes de notas
En la mayor parte del programa los parámetros entre funciones se repiten, y ello es porque las funciones se llaman constantemente entre sí y de la misma manera, el intercambio de datos debe ser constante.
"""

def calificaciones(numero_estudiantes, numero_notas, encabezado2, encabezado1, diccionario):
	"""
	Función encargada de generar la matriz principal que se usará durante la ejecución de todo el código.
	Los ciclos while se crearon con el objetivo de evitar que el programa entrará en un bucle y abortara la operación. Debido a que los datos tratados deben ser de un valor específico si se hace de otra manera el programa abortará
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
				while nombre.istitle() == False:
					nombre = input("Ingrese un(a) {} {} Válido: ".format(encabezado1, a+1))
				matriz_cal[a].append(nombre)
			else:
				while True:
					nota = input("{}, {} {}: ".format(nombre, encabezado2, b))
					try:
						nota = float(nota)
						break
					except ValueError:
						print()
						print("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, encabezado2, b))
						print()
					
				nota = round(float(nota), 2)
					
				matriz_cal[a].append(nota)

	print()
	print("Presione Cualquier Tecla Para Continuar...")
	wait()

	menu_de_seleccion(matriz_cal, encabezado1, encabezado2, numero_estudiantes, numero_notas, diccionario)


def notas(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):
	
	"""
	Función encargade de imprimir la tabla de notas actual con los datos presentes.
	:param int contador: variable encargada de indicar en el f-string el nombre del estudiante al cual las notas consecuntes perteneces
	:param list fila[]: itera entre las distintas sublistas presnentes en la matriz principal matriz_cal, para imprimir de manera individual sus valores al usuario en una misma fila
	:param obj elemento: encargado de iterar en todos los datos dentro de las sublistas definidas por fila para su posterior impresión con el uso de f-string
	:param function wait(): espera interacción del usuario para continuar antes de volver al menu principal denomidado menu_de_seleccion
	:param function encabezado(): sólo imprime el encabezado de la tabla en pantalla con los criterios dados al inicio del programa
	"""
	encabezado(parte1, parte2, diccionario)
	
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
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


def modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):
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
	:param function menu_de_seleccion: menu anterior para navegar en opciones distintas a la de modificación.6
	:param function notas_copia: permite visualizar los datos actuales sin necesidad de entrar a menús distintos.
	"""
	print()
	print("Este módulo es para modificar la información por estudiante.")
	print()
	print("Presione Cualquier Tecla para Continuar")
	print()
	wait()
	seleccion = input(("Ingrese M para modificar, N para volver, si desea ver los datos de la tabla, entonces T: ")).upper()
	
	while seleccion != "N" and seleccion != "T" and seleccion != "M":
		seleccion = input('Ingrese M para modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()

	print("{}, ¿es esto correcto?".format(seleccion))
	
	yes = input("(S/N): ").upper()
	
	while yes != "N" and yes != "S":
			yes = input("(S/N): ").upper()
	
	while yes == "N":
		seleccion = input(("Ingrese M para modificar, N para volver, si desea ver los datos de la tabla, entonces T: ")).upper()
	
		while seleccion != "N" and seleccion != "T" and seleccion != "M":
			seleccion = input('Ingrese M para modificar, N para volver, si desea ver los datos de la tabla, entonces T: ').upper()

		print("{}, ¿es esto correcto?".format(seleccion))
		yes = input("(S/N): ").upper()
		if yes == "S":
			continue
	
	if seleccion == "N":
		menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
	elif seleccion == "T":
		notas_copia(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
	elif seleccion == "M": 

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

		while seleccion2 != '0' and seleccion2 != '1' and seleccion2 != '2' and seleccion2 != '3':
			seleccion2 = input("Por favor seleccione una opción: ")
				
		yes = input(f"{seleccion2}, ¿Es esto Correcto?, (S/N): ").upper()
	
		while yes != "N" and yes != "S":
			yes = input("(S/N): ").upper()

		while yes == "N":
				seleccion2 = input("Por favor seleccione una opción: ")
				while seleccion2 != '0' and seleccion2 != '1' and seleccion2 != '2' and seleccion2 != '3':
					seleccion2 = input("Por favor seleccione una opción: ")
				yes = input(f"{seleccion2}, ¿Es esto Correcto?, (S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()

		seleccion2 = int(seleccion2)

		if seleccion2 == 0:

			modulo_cambio(matriz_cal, parte1, parte2,  numero_estudiantes, numero_notas, diccionario)

		if seleccion2 == 1:

			seleccion = input("Ingrese el Códgio de Estudiante a Revisar: ")
			while seleccion.isalnum() == False:
				seleccion = input("Ingrese el Códgio de Estudiante a Revisar Válido: ")

			while int(seleccion) > len(matriz_cal) or int(seleccion) == 0:
				seleccion = input("Ingrese el Códgio de Estudiante a Revisar Existente: ")
				while seleccion.isalnum() == False:
					seleccion = input("Ingrese el Códgio de Estudiante a Válido: ")

			seleccion = int(seleccion)-1
		
			print("El número {}, pertenece al estudiante {},". format(seleccion+1, matriz_cal[seleccion][0]), "¿está seguro que desea continuar?")
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
				yes = input("(S/N): ").upper()

			while yes == "N":
				seleccion = input("Ingrese el Códgio de Estudiante a Revisar: ")
				while seleccion.isalnum() == False:
					seleccion = input("Ingrese el Códgio de Estudiante a Revisar Válido: ")

				while int(seleccion) > len(matriz_cal) or int(seleccion) == 0:
					seleccion = input("Ingrese el Códgio de Estudiante a Revisar Existente: ")
					while seleccion.isalnum() == False:
						seleccion = input("Ingrese el Códgio de Estudiante a Revisar Válido: ")

				seleccion = int(seleccion)-1
		
				print("El número {}, pertenece al estudiante {},". format(seleccion+1, matriz_cal[seleccion][0]), "¿está seguro que desea continuar?")
				yes = input("(S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()

			seleccion1 = input("Por Favor Seleccione una Opción para Continuar, S para agregar notas o B para borrar: ").upper()

			while seleccion1 != "S" and seleccion1 != "B":
					seleccion1 = input("Por Favor Seleccione una Opción para Continuar, S para agregar notas o B para borrar: ").upper()

			if seleccion1 == "S": 
					
				while True:
					seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Adicionar: ")
					try:
						seleccion2 = int(seleccion2)
						break
					except ValueError:
						print()
						print("Ingrese un Valor Válido")
						print()

				seleccion2 = int(seleccion2)

				for b in range(seleccion2):
					while True:
						nota = input("{}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal)+b))
						try:
							nota = float(nota)
							break
						except ValueError:
							print()
							print("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, len(matriz_cal[seleccion])+b))
							print()
					
					nota = round(float(nota), 2)
					
					matriz_cal[seleccion].append(nota)

				print("Tarea realizada con éxtio, presione cualquier tecla para continuar: ")
				wait()
				modificar(matriz_cal, parte1, parte2,  numero_estudiantes, numero_notas, diccionario)

			if seleccion1 == "B": 
				while True:
					seleccion2 = input("Por Favor Ingrese Código de Nota a Borrar: ")
					try:
						seleccion2 = int(seleccion2)
						break
					except ValueError:
						print()
						print("Ingrese un Valor Válido")
						print()

				seleccion2 = int(seleccion2)

				print("Numero de nota seleccionada pertenece a {} de {}".format(matriz_cal[seleccion][0], matriz_cal[seleccion][seleccion2]),
		  "¿Desea continuar?")

				yes = input("(S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
				if yes == "N":
					modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)

				else:
					del(matriz_cal[seleccion][seleccion2])
					print("Tarea realizada con éxtio, presione cualquier tecla para continuar: ")
					wait()
					modificar(matriz_cal, parte1, parte2,  numero_estudiantes, numero_notas, diccionario)
			
		if seleccion2 == 2:

			notas_copia(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)

		if seleccion2 == 3:

			menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


def notas_copia(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):
	"""
	Copia de la función notas para uso específico de la función modifiar, se creo independiente debido a los problemas asociados a usar la misma función para ambos casos pues la originial volvía a menu_de_seleccion().
	:param int contador: variable encargada de indicar en el f-string el nombre del estudiante al cual las notas consecuntes perteneces
	:param sublist fila: itera entre las distintas sublistas presnentes en la matriz principal matriz_cal, para imprimir de manera individual sus valores al usuario en una misma fila
	:param obj elemento: encargado de iterar en todos los datos dentro de las sublistas definidas por fila para su posterior impresión con el uso de f-string
	:param function wait(): espera interacción del usuario para continuar antes de volver a función invocadora modificar()
	:param function encabezado(): sólo imprime el encabezado de la tabla en pantalla con los criterios dados al inicio del programa
	"""
	encabezado(parte1, parte2, diccionario)
	
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
	modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
				

def modulo_cambio(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):
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
	seleccion = input("Ingrese una opción; S para agregar nuevos datos, M para modificar datos: ").upper()

	while seleccion != "S" and seleccion != "M":
			seleccion = input("Ingrese una opción; agregar nuevos datos, S, para modificar datos, M: ").upper()

	if seleccion == "S":
		while True:
			numero_estudiantes1 = input("Por Favor Indique Cuántos Estudiantes a Agregar: ")
			try:
				numero_estudiantes1 = int(numero_estudiantes1)
				break
			except ValueError:
				print()
				print("Por Favor Ingrese un Número Válido")
				print()

		numero_estudiantes1 = int(numero_estudiantes1)

		while True:
			numero_notas1 = input("Por Favor Indique Cuántas Notas por Estudiante Nuevo se van a Agregar: ")
			try:
				numero_notas1 = int(numero_notas1)
				break
			except ValueError:
				print()
				print("Por Favor Ingrese un Número Válido")
				print

		numero_notas1 = int(numero_notas1)

		for a in range(numero_estudiantes1):
			matriz_cal.append([])
			for b in range(numero_notas1+1):
				if b == 0:
					nombre = input("{} {}: ".format(parte1, numero_estudiantes+a+1))
					while nombre.istitle() == False:
						nombre = input("Ingrese un(a) {} {} Válido: ".format(parte1, numero_estudiantes+a+1))
					matriz_cal[a+numero_estudiantes].append(nombre)
				else:
					while True:
						nota = input("{}, {} {}: ".format(nombre, parte2, b))
						try:
							nota = float(nota)
							break
						except ValueError:
							print()
							print("Ingrese un Valor Válido para {}, {} {}: ".format(nombre, parte2, b))
					nota = round(float(nota), 2)
					matriz_cal[a+numero_estudiantes].append(nota)

		print("Presione Cualquier Tecla Para Continuar...")
		wait()

		modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)

	elif seleccion == "M":
		seleccion = input("Por Favor Ingrese el Código de Estudiante a ser Modificado: ")
		while seleccion.isnumeric() == False:
			seleccion = input("Por Favor Ingrese el Código de Estudiante a ser Modificado Válido: ")

		while int(seleccion) > len(matriz_cal) or int(seleccion) == 0:
			seleccion = input("Por Favor Ingrese un Código Existente de Estudiante: ")
			while seleccion.isalnum() == False:
				seleccion = input("Por Favor Ingrese el Código de Estudiante a ser Modificado Válido: ")

		seleccion = int(seleccion)-1

		print(f"El Valor {seleccion+1} pertenece al estudiante {matriz_cal[seleccion][0]}, ¿está seguro que desea continuar?")

		yes = input("S/N: ").upper()
		while yes != "S" and yes != "N":
			yes = input('S/N: ').upper()

		while yes == "N":
			seleccion = input("Por Favor Ingrese el Código de Estudiante a ser Modificado: ")
			while seleccion.isalnum() == False:
				seleccion = input("Por Favor Ingrese el Código de Estudiante a ser Modificado Válido: ")

			while int(seleccion) > len(matriz_cal) or int(selccion) == 0:
				seleccion = input("Por Favor Ingrese un Código Existente de Estudiante: ")
				while seleccion.isalnum() == False:
					seleccion = input("Por Favor Ingrese el Código de Estudiante a ser Modificado Válido: ")

			seleccion = int(seleccion)-1

			print(f"El Valor {seleccion+1} pertenece al estudiante {matriz_cal[seleccion][0]}, ¿está seguro que desea continuar?")

			yes = input("S/N: ").upper()
			while yes != "S" and yes != "N":
				yes = input('S/N: ').upper()
		
		seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Modificar, E, para hacerlo por código de nota o N para cambiar el nombre: ").upper()
				
		while seleccion2.isnumeric() == False and seleccion2 != "E" and seleccion2 != "N" :
			seleccion2 = input("Por Favor Ingrese Cantidad de Notas a Modificar, E, para hacerlo por código de nota o N para cambiar el nombre: ").upper()
					 
		if seleccion2 == "E":			
			seleccion2 = input("Ingrese el Código de Nota a ser Modificado: ")
			 
			while seleccion2.isnumeric() == False:
				seleccion2 = input("Ingrese un Código de Nota Válido: ")

			while int(seleccion2) > len(matriz_cal[seleccion]):
				seleccion2 = input("Ingrese un Código de Nota Válido: ")
				while seleccion2.isnumeric() == False:
					seleccion2 = input("Ingrese un Código de Nota Válido: ")
				

			seleccion2 = int(seleccion2)

			
			while True:
				nota = input("{}, {} {}: ".format(matriz_cal[seleccion][0], parte2, seleccion2-1))
				try:
					nota = float(nota)
					break
				except ValueError:
					print()
					print("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, seleccion2-1))
					print()
							
			nota = round(float(nota), 2)
					
			matriz_cal[seleccion][seleccion2] = nota
			print()
			print("Presione Cualquier Tecla Para Continuar...")
			wait()
			modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


		elif seleccion2 == "N":

			
			nombre = input("Ingrese nuevo {}, {}: ".format( parte1, matriz_cal[seleccion][0]))

			matriz_cal[seleccion][0] = nombre
			print()
			print("Presione Cualquier Tecla Para Continuar...")
			wait()

			modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)



		else: 
			seleccion2 = int(seleccion2)
			while len(matriz_cal[seleccion])-1 < seleccion2:
				print("Valor Ingresado Fuera de Rango")
				while True:
					seleccion2 = input("Ingrese un Número Válido: ")
					try:
						seleccion2 = int(seleccion2)
						break
					except ValueError:
						print()
						print("Ingrese un Valor Válido")
						print()

			for b in range(seleccion2):
				while True:
					nota = input("{}, {} {}: ".format(matriz_cal[seleccion][0], parte2, b+1))
					try:
						nota = float(nota)
						break
					except ValueError:
						print()
						print("Ingrese un Valor Válido para {}, {} {}: ".format(matriz_cal[seleccion][0], parte2, b+1))
						print()
				nota = round(float(nota), 2)
				matriz_cal[seleccion][b+1] = nota

			print()
			print("Presione Cualquier Tecla Para Continuar...")
			wait()

			modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


def final(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):

	"""
	Se encarga de mostrar la nota deifinitiva para el periodo de tiempo especificado acorde a la totalidad de notas. Cada nota tiene el mismo peso, no se puede realizar sobre procentajes.
	:param string parte3: cambio del valor de la tabla del encabezado para desglosar el texto especidicado.
	:param function encabezado(): función que imprime el encabezado de la tabla.
	:param int contador: iterador para el f-string 
	:param int contador1: acumula valores a ser divididos para la obtención de la nota final
	:param int suma: valor final de la calificación.
	:param function wait(): espera una respuesta del usuario para continuar con la ejecución del código.
	:param function menu_de_seleccion(): regresa al menu de opción del reporte.
	"""


	parte3 = "Notas Finales (ponderado)"

	encabezado(parte1, parte3, diccionario)

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
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


def menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):
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
	print("                5. Guardar el Archivo")
	print()
	print("                6. Salir")
	print()

	seleccion = input("Ingrese una Opción: ")

	while seleccion != '0' and seleccion!= '1' and seleccion != '2' and seleccion != "3" and seleccion != "4" and seleccion != "5" and seleccion != "6":
		seleccion = input("Ingrese una Opción: ")
	
		
	print(str(seleccion) + ", ¿es esta opción correcta?")
	
	
	yes = input("(S/N): ").upper()
	
	while yes != "S" and yes != "N":
		yes = input("(S/N): ").upper()

	if yes == "S":
			
		if seleccion == "2":
			notas(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "0":
			final(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "1":
			tabla(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "3":
			diagrama(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "4":
			modificar(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "6":
			main1(diccionario)
		else:
			nombre1 = input("Ingrese Nombre del Archivo (con extensión): ")
			h = open(nombre1, "w")
			h.write(str(matriz_cal))
			h.write("\n"+str(parte1))
			h.write("\n"+str(parte2))
			h.write("\n"+str(numero_notas))
			h.write("\n"+str(numero_estudiantes))
			h.close()
			menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


	
	elif yes == "N":
		menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


def tabla(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):
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

	
	while True:
		seleccion = input("Por Favor Ingrese Código {} a Revisar: ".format(parte1))
		try:
			seleccion = int(seleccion)
			break
		except ValueError:
			print()
			print("Ingrese un número de {} válido.".format(parte1))
			print()
	
	while int(seleccion) > len(matriz_cal):
		print("Ingrese un número de {} existente.".format(parte1))
		while True:
			seleccion = input("Por Favor Ingrese Código {} a Revisar: ".format(parte1))
			try:
				seleccion = int(seleccion)
				break
			except ValueError:
				print()
				print("Ingrese un número de {} válido: ".format(parte1))
				print()

	print("El código {}, pertenece al estudiante {}, ¿es esto correcto?".format(seleccion, matriz_cal[int(seleccion)-1][0]))

	yes = input("S/N: ").upper()

	while yes != "S" and yes != "N":
		yes = input("S/N: ").upper()

	while yes == "N":
		while True:
			seleccion = input("Por Favor Ingrese Código {} a Revisar: ".format(parte1))
			try:
				seleccion = int(seleccion)
				break
			except ValueError:
				print()
				print("Ingrese un número de {} válido.".format(parte1))
				print()
	
		while int(seleccion) > len(matriz_cal) or int(seleccion) == 0:
			print("Ingrese un número de {} existente.".format(parte1))
			while True:
				seleccion = input("Por Favor Ingrese Código {} a Revisar: ".format(parte1))
				try:
					seleccion = int(seleccion)
					break
				except ValueError:
					print()
					print("Ingrese un número de {} válido.".format(parte1))
					print()

		print("El código {}, pertenece al estudiante {}, ¿es esto correcto?".format(seleccion, matriz_cal[int(seleccion)-1][0]))

		yes = input("S/N: ").upper()

		while yes != "S" and yes != "N":
			yes = input("S/N: ").upper()


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
	if len(matriz_alv) < 3:
		axs.plot(matriz_terciaria[1:], matriz_alv[1:], 'o', color = 'red', label= 'Rendimiento {}'.format(matriz_secundaria[0]))
		fig.suptitle(f'Rendimiento {matriz_secundaria[0]}')
		plt.ylabel("Nota Obtenida")
		plt.xlabel("Número Nota")
		plt.legend()
		plt.grid()
		plt.show()
	else:
		axs.plot(matriz_terciaria[1:], matriz_alv[1:], color = 'red', label= 'Rendimiento {}'.format(matriz_secundaria[0]))
		fig.suptitle(f'Rendimiento {matriz_secundaria[0]}')
		plt.ylabel("Nota Obtenida")
		plt.xlabel("Número Nota")
		plt.legend()
		plt.grid()
		plt.show()
		



	input("Presione Cualquier Tecla para Continuar...")

	wait()
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)


def diagrama(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario):

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
	menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)

def encabezado(Parte1, Parte2, diccionario):
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


def main1(diccionario):
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
	print("                 2. Cargar Archivo de Reporte")
	print()
	print("                 3. Volver al Menu anterior")
	print()
	
	print("Seleccione una opción para continuar: ", end = "")
	seleccion = input()
	

	while seleccion != "1" and seleccion != "2" and seleccion != "3":
		print("Seleccione una opción válida: ", end="")
		seleccion = input()

	print(str(seleccion) + ", ¿es esta opción correcta?")
	yes = input("(S/N): ").upper()

	while yes != "S" and yes != "N":
		yes = input("(S/N): ").upper()
	
	if yes == "S":

		if seleccion == "3":
			usuarios(diccionario)

		elif seleccion == "1":
			print("Para iniciar, por favor presione cualquier tecla...")
			wait()
			print()

			
			while True:
				numero_estudiantes = input('Ingrese Cantidad de Estudiantes: ')
				try:
					numero_estudiantes = int(numero_estudiantes)
					break
				except ValueError:
					print()
					print("Cantidad Inválida de Estudiantes")
					print()
						
			numero_estudiantes = int(numero_estudiantes)
			print()
			print("{}, ¿es esto correcto?".format(numero_estudiantes))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
			while yes == "N":
				while True:
					numero_estudiantes = input('Ingrese Cantidad de Estudiantes: ')
					try:
						numero_estudiantes = int(numero_estudiantes)
						break
					except ValueError:
						print()
						print("Cantidad Inválida de Estudiantes")
						print()
						

				numero_estudiantes = int(numero_estudiantes)
				print("{}, ¿es esto correcto?".format(numero_estudiantes))
				yes = input("(S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			
			
			while True:
				numero_notas = input('Ingrese Total de Notas: ')
				try:
					numero_notas = int(numero_notas)
					break
				except ValueError:
					print()
					print('Total Inválido de Notas')
					print()

			numero_notas = int(numero_notas)
			print()
			print("{}, ¿es esto correcto?".format(numero_notas))
			yes = input("(S/N): ").upper()
			
			while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
			
			while yes == "N":
				while True:
					numero_notas = input('Ingrese Total de Notas: ')
					try:
						numero_notas = int(numero_notas)
						break
					except ValueError:
						print()
						print('Total Inválido de Notas')
						print()
						
				numero_notas = int(numero_notas)
				print("{}, ¿es esto correcto?".format(numero_notas))
				yes = input("(S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			
			Parte1= input("Por Favor Ingrese Criterio de tabla 1 (Columna de Notas): ")

			while Parte1.istitle() == False:
				Parte1 = input('Por Favor Ingrese Criterio tabla 1 Válido (Formato de Título: Notas, etc...): ')
				

			print("{}, ¿es esto correcto?".format(Parte1))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
			while yes == "N":
				Parte1= input("Por Favor Ingrese Criterio de tabla 1 (Columna de Notas): ")
				while Parte1.istitle() == False:
					Parte1 = input('Por Favor Ingrese Criterio tabla 1 Válido (Formato de Título: Notas, etc...): ')

				print("{}, ¿es esto correcto?".format(Parte1))
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
				yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			print()
			Parte2 = input("Por Favor Ingrese Criterio tabla 2 (Columna de Nombre del Estudiante): ")

			while Parte2.istitle() == False:
				Parte2 = input('Por Favor Ingrese Criterio tabla 2 Válida (Formato de Título: Nombre, etc...): ')

			print("{}, ¿es esto correcto?".format(Parte2))
			yes = input("(S/N): ").upper()
			while yes != "N" and yes != "S":
				yes = input("(S/N): ").upper()
			while yes == "N":
				Parte2 = input("Por Favor Ingrese Criterio tabla 2 (Columna de Nombre del Estudiante): ")

				while Parte2.istitle() == False:
					Parte2 = input('Por Favor Ingrese Criterio tabla 2 Válida (Formato de Título: Nombre, etc...): ')

				print("{}, ¿es esto correcto?".format(Parte2))
				yes = input("(S/N): ").upper()
				while yes != "N" and yes != "S":
					yes = input("(S/N): ").upper()
				if yes == "S":
					continue
			print()
			calificaciones(numero_estudiantes, numero_notas, Parte1, Parte2, diccionario)
		else:
			arch = input("Por Favor Indique el nombre del Archivo (con la extensión): ")
			try:
				h = open(arch, "r")
			except:
				print("Nombre archivo inexistente, presione cualquier tecla para continuar...")
				wait()
				main1(diccionario)			
			hola = str(h.readline())
			hola = hola[:-1]
			encabezado1 = str(h.readline())
			encabezado1 = encabezado1[:-1]
			encabezado2 = str(h.readline())
			encabezado2 = encabezado2[:-1]
			numero_notas = int(h.readline())
			numero_estudiantes = int(h.readline())
			h.close()
			matriz_cal = lector(hola, numero_estudiantes, numero_notas, diccionario)
			print("Proceso completado, presione cualquier tecla para continuar...")
			wait()
			menu_de_seleccion(matriz_cal, encabezado1, encabezado2, numero_estudiantes, numero_notas, diccionario)
	elif yes == "N":
		main1(diccionario)


def lector(hola, numero_estudiantes, numero_notas, diccionario):
	"""
	Este es el módulo encargado de leer los archivos para el generador de reportes, 
	en este caso sólo se encarga de leer la matriz principal usada en el programa definida como "matriz_cal", que al guardarse se vuelve un tipo string
	"""
	hola = [hola[1:-1]]
	matriz = []
	matriz_cal = []
	nombre = ""
	contador = 0
	contador2 = 0
	st = True
	for elemento in hola:
		for numero in range(len(elemento)):
			if elemento[numero] == "]":
				matriz.append(float(nombre))
				nombre = ""
				matriz_cal.append(matriz[:])
				matriz = []
				st = True
			elif elemento[numero]  == "'":
				contador += 1
				if contador == 2:
					st = False
					contador = 0
					matriz.append(nombre)
					nombre = ""
			elif (elemento[numero].isalpha() == True or (elemento[numero] == " " and elemento[numero+1] != "[")) and st:
				nombre += elemento[numero]
			elif elemento[numero] == "," and elemento[numero-1] != "]":
				contador2+=1
				if contador2 == 2:
					contador2 = 0
					matriz.append(float(nombre))
					nombre = ""
					st = True
			elif elemento[numero].isnumeric() == True or elemento[numero] == ".":
				nombre += elemento[numero]
	
	return matriz_cal

def usuarios(diccionario):
	"""
	Este es el módulo de inicio de sesión previo a la interfaz del programa
	Cada uno de los parámetros en el pertenecen a una variable que posteriormente se guardará en un diccionariio, dependiendo del mismo es el acceso 
	que se le da al usuario.

	"""
	print()
	print("                MENU PRINCIPAL")
	print()
	print("           1. Ingresar")
	print()
	print("           2. Registrarse")
	print()
	seleccion = input("Ingrese una opción: ")
	while seleccion != "1" and seleccion != "2":
		seleccion = input("Ingrese una opción válida: ")

	if seleccion == "2":
		hola = input("Indique el tipo de usuario (usuario o administrador): ").upper()
		while hola != 'USUARIO' and hola != 'ADMINISTRADOR':
			hola = input("Indique el tipo de usuario (usuario o administrador): ").upper()

		if hola == "USUARIO":
			cantidad = 1
			diccionario = {}
			for numero in range(cantidad):
				nombre_usuario = input("Ingrese un nuevo nombre de usuario {}: ".format(numero+1))
				diccionario[nombre_usuario] = input("Ingrese valor contraseña para {}: ".format(nombre_usuario))
		if hola == "ADMINISTRADOR":
			cantidad = input("Ingrese el número de usuarios a agregar: ")
			while cantidad.isnumeric() == False:
				cantidad = input("Ingrese un valor de usuarios válido: ")
			cantidad = int(cantidad)
			diccionario = {}
			for numero in range(cantidad):
				nombre_usuario = input("Ingrese un nuevo nombre de usuario {}: ".format(numero+1))
				diccionario[nombre_usuario] = input("Ingrese valor contraseña para {}: ".format(nombre_usuario))
		usuarios(diccionario)

	if seleccion == "1":
		if len(diccionario)<1:
			print("Actualmente sin usuarios, volviendo al menú principal...")
			usuarios(diccionario)
		print("Bienvenido a la interfaz de incio de sesión")
		hola = input("Indique el tipo de usuario (usuario o administrador): ").upper()
		while hola != 'USUARIO' and hola != 'ADMINISTRADOR':
			hola = input("Indique el tipo de usuario (usuario o administrador): ").upper()
		nombre = (input("Por favor Ingrese su nombre de usuario: "))
		while nombre not in diccionario:
			nombre = (input("El usuario no existe, ingrese un usuario existente: "))
		contra = (input("Ingrese la contraseña: "))
		limites = 3
		while diccionario[nombre] != contra:
			limites -= 1
			print("Contraseña incorrecta, intentos restantes{}".format(limites))
			contra = (input("Ingrese la contraseña: "))
			if limites == 0:
				print("El usuario {}, ha sido bloqueado.".format(nombre))
				break
		if limites == 0:
			print("Reinicie para volver a acceder al usuario")
		else:
			print("Bienvenido {}".format(nombre))
			if hola == "ADMINISTRADOR":
				main1(diccionario)
			elif hola == "USUARIO":\
				restricted(diccionario)


def restricted(diccionario):
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
	print("                 1. Cargar Archivo de Reporte")
	print()
	print("                 2. Volver al Menu anterior")
	print()
	
	print("Seleccione una opción para continuar: ", end = "")
	seleccion = input()
	

	while seleccion != "1" and seleccion != "2" and seleccion != "3":
		print("Seleccione una opción válida: ", end="")
		seleccion = input()

	print(str(seleccion) + ", ¿es esta opción correcta?")
	yes = input("(S/N): ").upper()

	while yes != "S" and yes != "N":
		yes = input("(S/N): ").upper()
	
	if yes == "S":

		if seleccion == "2":
			usuarios(diccionario)

		else:
			arch = input("Por Favor Indique el nombre del Archivo (con la extensión): ")
			try:
				h = open(arch, "r")
			except:
				print("Nombre archivo inexistente, presione cualquier tecla para continuar...")
				wait()
				main1(diccionario)			
			hola = str(h.readline())
			hola = hola[:-1]
			encabezado1 = str(h.readline())
			encabezado1 = encabezado1[:-1]
			encabezado2 = str(h.readline())
			encabezado2 = encabezado2[:-1]
			numero_notas = int(h.readline())
			numero_estudiantes = int(h.readline())
			h.close()
			matriz_cal = lector(hola, numero_estudiantes, numero_notas)
			print("Proceso completado, presione cualquier tecla para continuar...")
			wait()
			menu_de_seleccion_res(matriz_cal, encabezado1, encabezado2, numero_estudiantes, numero_notas, diccionario)
	elif yes == "N":
		main1(diccionario)

def menu_de_seleccion_res(matriz_cal, encabezado1, encabezado2, numero_estudiantes, numero_notas, diccionario):
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
	print("                4. Salir")
	print()

	seleccion = input("Ingrese una Opción: ")

	while seleccion != '0' and seleccion!= '1' and seleccion != '2' and seleccion != "3" and seleccion != "4":
		seleccion = input("Ingrese una Opción: ")
	
		
	print(str(seleccion) + ", ¿es esta opción correcta?")	
	
	yes = input("(S/N): ").upper()
	
	while yes != "S" and yes != "N":
		yes = input("(S/N): ").upper()

	if yes == "S":
			
		if seleccion == "2":
			notas(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "0":
			final(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "1":
			tabla(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		elif seleccion == "3":
			diagrama(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)
		else:
			main1(diccionario)	
	elif yes == "N":
		menu_de_seleccion(matriz_cal, parte1, parte2, numero_estudiantes, numero_notas, diccionario)

usuarios(diccionario)

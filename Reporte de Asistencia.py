import msvcrt as m

import matplotlib.pyplot as plt


def menu_main():
	print("	           REPORTE DE ASISTENCIA")
	print("                    ===================")
	print()
	print("              Bienvenido al reporte de asistencia")
	print()
	print("              1. Nuevo Reporte")
	print()
	print("              2. Cargar Archivo de Reporte")
	print()
	print("              3. Volver al Menu anterior")
	print()

	seleccion = input("Ingrese una opción: ")
	while seleccion != "1" and seleccion != "2" and seleccion != "3":
		seleccion = input("Ingrese una opción válida:   ")

	if seleccion == "1":
		nueva()
	if seleccion == "2":
		cargar()
	if seleccion == "3":
		exit()

def nueva():
	print("	         OPCIONES DE REPORTE")
	print("                    ===================")
	print()
	print("          1. Reporte Estándar de Colegio (sólo nombre)")
	print()
	print("          2. Reporte Empresarial de Asistencia (nombre y código de Empleado)")
	print()
	print("          3. Volver al Menu Anterior")
	print()
	
	seleccion = input("Ingrese el tipo de reporte de asistencia: ")
	while seleccion != "1" and seleccion != "2" and seleccion != "3":
		seleccion = input("Ingrese una opción válida: ")

	if seleccion == "1":
		opcion = "C"
		col(opcion)
	if seleccion == "2":
		opcion == "E"
		emp(opcion)
	if seleccion == "3":
		menu_main()


def emp(opcion):
	planilla = {}
	while True:
		cant = input("Ingrese número de empleados: ")
		try:
			cant = int(cant)
			break
		except ValueError:
			print ("Ingrese un número válido.")
	for numero in range(cant):
		nombre = input("Ingrese el nombre del empleado {}: ".format(numero+1))
		while nombre.istitle() == False:
			nombre = input("Ingrese un nombre válido {}: ".format(numero+1))
		codigo = input("Ingrese códdigo de empleado {}: ".format(nombre))
		while codigo.isnumeric() == False:
			codigo = input("Ingrese códdigo válido para {} (sólo números): ".format(nombre))
		planilla[nombre] = codigo
		planilla[nombre]["reporte"]=[]
		planilla[nombre]["reporte"].append(0)
		planilla[nombre]["reporte"].append(0)
		planilla[nombre]["reporte"].append(0)
	
	menu(planilla, opcion)

def col(opcion):
	planilla = {}
	while True:
		cant = input("Ingrese número de estudiantes: ")
		try:
			cant = int(cant)
			break
		except ValueError:
			print("Ingrese un número válido.")
	for numero in range(cant):
		nombre = input("Ingrese el nombre estudiante {}: ".format(numero+1))
		while nombre.istitle() == False:
			nombre = input("Ingrese nombre válido estudiante {}: ".format(numero+1))
		planilla[nombre] = numero
		planilla[nombre]["reporte"]=[]
		planilla[nombre]["reporte"].append(0)
		planilla[nombre]["reporte"].append(0)
		planilla[nombre]["reporte"].append(0)
	menu(planilla, opcion)

def menu(planilla, opcion):
	if opcion == "C":
		encabezado = ["Código", "Nombre Estudiante", "Asistencia", "Fallos", "Tardanzas"]
	if opcion == "E":
		encabezado = ["Empleado", "Nombre Personal", "Asistencia", "Fallos", "Tardanzas"]

	print("	                        OPCIONES")
	print("                    ===================")
	print()
	print("              Bienvenido al reporte de asistencia")
	print()
	print("              1. Agregar Información")
	print()
	print("              2. Cambiar Datos")
	print()
	print("              3. Volver al Menu anterior")
	print()
	print("              4. Generar Diagrama Comportamiento de Empleado")
	print()
	print("              5. Comportamiento General del Personal")
	print()
	print("              6. Tabla con Datos de Entrada")
	print()


menu_main()
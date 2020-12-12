import tkinter as tk
from tkinter import ttk
from tkinter import *


import tkinter as tk

menu = tk.Tk()
menu.title("Generador de Reportes - Grupo 9")
menu.geometry("700x500")
menu.configure(background = "white")

label = Label(menu,text="Generador de reportes",font=("Times New Roman",30),background=("White"))
label.pack(side="top",padx=30,pady=30)

label2 = Label(menu,text="Hecho por: Juan David Ramirez Lopez, Daniel E. Ballén Baena, D. Felipe Lancheros Ramirez"+"\n"+"Grupo 9",font=("Times New Roman",10),background=("white"))
label2.pack(side="bottom",padx=30,pady=30)

var=tk.StringVar(menu)
var.set("Seleccione un reporte")
opciones = ["Reporte de asistencia", "Reporte de tabla de campeonato de futbol", "Reporte de notas"]
opcion=tk.OptionMenu(menu,var,*opciones)
opcion.config(width=40)
opcion.pack(side="top",padx=30,pady=30)

o1 = tk.Label(menu,text="Usted a seleccionado:",font=("Times New Roman",20),bg=("white"))
o1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
reporte=tk.Label(menu,bg="cyan",textvariable=var,padx=5,pady=5,width=50)
reporte.pack()

def createNewWindow():
    ventana = tk.Toplevel(menu)
    ventana.title("Generador de Reportes - Grupo 9")
    ventana.geometry("700x500")
    ventana.configure(background="white")

menu.button = ttk.Button(menu, text="¡Ir alla!",
              command=createNewWindow)
menu.button.pack()
menu.button.place(x=300, y=350,width=100,height=40)

menu.mainloop(

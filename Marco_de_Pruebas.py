from tkinter import *

def ventana_principal():
    raiz = Tk()
    raiz.title("Generador de Reportes")
    raiz.resizable(False, False)
    raiz.geometry('750x500')
    raiz.config(bg='blue', relief = 'sunken', bd = '2', cursor = 'circle')
    etiqueta = Label(raiz, text = "Menú Principal Generador de Reportes", bg='gray')
    etiqueta.pack(side= BOTTOM, fill = X)
    etiqueta2 = Label(raiz, text = "Bienvenidos al Generador de Reportes", font=('Arial Bold',15), fg='white', bg='blue')
    etiqueta2.pack(side= TOP)
    frame_menuprincipal=Frame() 
    frame_menuprincipal.pack(expand = '0')
    frame_menuprincipal.config(bg='white', width="700", height="450", relief = "groove", bd = "10",
                               cursor = 'pirate')
    labelprincipal = Label(frame_menuprincipal, text="1. Crear un Nuevo Reporte", font=("Arial", 10),
                           )
    labelprincipal.grid(row = '0', column = '0')

    raiz.mainloop()


ventana_principal()

def interfaz():
    contador = 0
    #con esto se abrirá una ventana
    ventana = Tk()
    etiqueta = Label(ventana, text = "Reporte", bg='gray')
    etiqueta.pack(side= BOTTOM, fill = X)
    etiqueta2 = Label(ventana, text = "Bienvenidos al Generador de Reportes", font=('Arial Bold',15))
    etiqueta3 = Label(ventana, text= "Por favor seleccione una opción", font=('Arial', 10))
    ventana.mainloop()


def main():
    ventana_principal()
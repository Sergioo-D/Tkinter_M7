from tkinter import filedialog as quelcom
import os
import tkinter
from PIL import ImageTk, Image

lista_imagenes = []

index = 0
foto = None

def muestraImagenes(index):
    global foto
    if 0 <= index < len(lista_imagenes):
        foto = Image.open(os.path.join(lista_imagenes, lista_imagenes[index]))
        foto = ImageTk.PhotoImage(foto)
        label.config(image=foto)
        label.image = foto
        boton_atras.config(state=tkinter.NORMAL if index > 0 else tkinter.DISABLED)
        boton_alante.config(state=tkinter.NORMAL if index < len(lista_imagenes) - 1 else tkinter.DISABLED)

def cargarImagenes():
    global foto
    ruta_imagen = quelcom.askopenfilename(initialdir=os.getcwd(), filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")])
    if ruta_imagen:
        foto = Image.open(ruta_imagen)
        foto = ImageTk.PhotoImage(foto)
        label.config(image=foto)
        label.image = foto
        boton_atras.config(state=tkinter.DISABLED)
        boton_alante.config(state=tkinter.DISABLED)

def siguiente():
    global index
    if index < len(lista_imagenes) - 1:
        index += 1
        muestraImagenes(index)

def anterior():
    global index
    if index > 0:
        index -= 1
        muestraImagenes(index)

def cerrarVentana():
    finestra.destroy()

finestra = tkinter.Tk()
finestra.geometry("500x300")

boton_abrir = tkinter.Button(finestra, text="Abrir Carpeta", command=cargarImagenes)
boton_alante = tkinter.Button(finestra, text="Siguiente", command=siguiente)
boton_atras = tkinter.Button(finestra, text="Anterior", command=anterior, state=tkinter.DISABLED)
boton_salir = tkinter.Button(finestra, text="Salir", command=cerrarVentana)

boton_abrir.place(x=50, y=10)
boton_alante.place(x=50, y=50)
boton_atras.place(x=50, y=150)
boton_salir.place(x=50, y=250)

label = tkinter.Label(finestra)
label.place(x=200, y=50)

finestra.mainloop()
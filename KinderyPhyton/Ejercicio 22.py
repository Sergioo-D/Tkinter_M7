from tkinter import filedialog as quelcom
import os
import tkinter
from PIL import ImageTk, Image

ruta_imagen = None


def abrirImagen():
    global ruta_imagen
    ruta_imagen = quelcom.askopenfilename(initialdir=os.getcwd(),
                                          filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")])
    if ruta_imagen:
        mostrarImagen(ruta_imagen)



def mostrarImagen(ruta_imagen):
    ventana_secundaria = tkinter.Toplevel()
    ancho = 500
    largo= 300
    ventana_secundaria.geometry(f"{ancho}x{largo}")

    ruta_label = tkinter.Label(ventana_secundaria, text="Ruta de la imagen: " + ruta_imagen)
    ruta_label.pack()

    foto = Image.open(ruta_imagen)
    foto = ImageTk.PhotoImage(foto)
    imagen_label = tkinter.Label(ventana_secundaria, image=foto)
    imagen_label.image = foto
    imagen_label.pack()


finestra = tkinter.Tk()
ancho = 500
largo = 300
finestra.geometry(f"{ancho}x{largo}")

boton_abrir = tkinter.Button(finestra, text="Abrir Imagen", command=abrirImagen)
boton_abrir.pack()

finestra.mainloop()
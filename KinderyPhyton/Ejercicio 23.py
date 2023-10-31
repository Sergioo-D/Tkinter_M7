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
    largo = 300
    ventana_secundaria.geometry(f"{ancho}x{largo}")

    ruta_label = tkinter.Label(ventana_secundaria, text="Ruta de la imagen: " + ruta_imagen)
    ruta_label.pack()

    foto = Image.open(ruta_imagen)
    foto = ImageTk.PhotoImage(foto)
    imagen_label = tkinter.Label(ventana_secundaria, image=foto)
    imagen_label.image = foto
    imagen_label.pack()

    boton_guardar = tkinter.Button(ventana_secundaria, text="Guardar Imagen", command=lambda: guardarImagen(ruta_imagen))
    boton_guardar.pack()


def guardarImagen(ruta_imagen):
    ruta_guardar = quelcom.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if ruta_guardar:
        imagen = Image.open(ruta_imagen)
        imagen.save(ruta_guardar)


finestra = tkinter.Tk()
ancho = 500
largo = 300
finestra.geometry(f"{ancho}x{largo}")

boton_abrir = tkinter.Button(finestra, text="Abrir Imagen", command=abrirImagen)
boton_abrir.pack()

finestra.mainloop()
import tkinter
from tkinter import SUNKEN

from PIL import ImageTk, Image

directorio = "./foto"
lista_imagenes = ["1.png", "2.png", "3.png", "4.png", "5.png"]

index = 0
foto = None

def muestraImagenes():
    global foto
    if 0 <= index < len(lista_imagenes):
        foto = Image.open(f"{directorio}/{lista_imagenes[index]}")
        foto = ImageTk.PhotoImage(foto)
        label.config(image=foto)
        label.image = foto
        boton_atras.config(state=tkinter.NORMAL if index > 0 else tkinter.DISABLED)
        contador = tkinter.Label(finestra, anchor="e", bd=5, text=str(index + 1) + "/" + str(len(lista_imagenes)),
                                 relief=SUNKEN)
        contador.place(x=450, y=250)

def siguiente():
    global index
    if index < len(lista_imagenes) - 1:
        index += 1
        muestraImagenes()

def anterior():
    global index
    if index > 0:
        index -= 1
        muestraImagenes()

def cerrarVentana():
    finestra.destroy()

finestra = tkinter.Tk()
finestra.geometry("500x300")
finestra.configure(background="pink")

contador = tkinter.Label(finestra,anchor="e",bd=5,text= str(index + 1) + "/" + str(len(lista_imagenes)),relief=SUNKEN)
contador.place(x=450, y=250)


boton_alante = tkinter.Button(finestra, text="Siguiente", command=siguiente,bg="yellow",fg="black")
boton_atras = tkinter.Button(finestra, text="Anterior", command=anterior,state=tkinter.DISABLED,bg="yellow",fg="black")
boton_salir = tkinter.Button(finestra, text="Salir", command=cerrarVentana,bg="yellow",fg="black")

boton_alante.place(x=50, y=50)
boton_atras.place(x=50, y=150)
boton_salir.place(x=50, y=250)

label = tkinter.Label(finestra)
label.place(x=200, y=50)

muestraImagenes()

finestra.mainloop()
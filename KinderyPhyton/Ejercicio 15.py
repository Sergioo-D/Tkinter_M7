import tkinter
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
finestra.geometry("600x400")

miFrame = tkinter.LabelFrame(finestra, text="Mis botones", padx=10, pady=10)
miFrame.pack(pady=20)

boton_alante = tkinter.Button(miFrame, text="Siguiente", command=siguiente)
boton_atras = tkinter.Button(miFrame, text="Anterior", command=anterior, state=tkinter.DISABLED)
boton_salir = tkinter.Button(miFrame, text="Salir", command=cerrarVentana)

boton_alante.grid(row=0, column=0, padx=10)
boton_atras.grid(row=0, column=1, padx=10)
boton_salir.grid(row=0, column=2, padx=10)

label = tkinter.Label(finestra)
label.pack()

muestraImagenes()

finestra.mainloop()
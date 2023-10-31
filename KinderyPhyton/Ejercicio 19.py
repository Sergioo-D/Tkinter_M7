import tkinter
from tkinter import messagebox

finestra = tkinter.Tk()
ancho = 200
largo = 200
finestra.geometry(f"{ancho}x{largo}")

ask = messagebox.askquestion("Prueba", "Holaaaa")
askancel = messagebox.askokcancel("Prueba", "Holaaaa")
sino = messagebox.askyesno("Prueba", "Holaaaa")


def canviar_text(etiqueta, resposta):
    if resposta == "yes":
        etiqueta.config(text="Has clicat sí")
    elif resposta == 1:
        etiqueta.config(text="Has clicat sí")
    else:
        etiqueta.config(text="Has clicat no")

etiqueta1 = tkinter.Label(finestra, text="",fg="green")
etiqueta1.pack()
etiqueta2 = tkinter.Label(finestra, text="",fg="purple")
etiqueta2.pack()
etiqueta3 = tkinter.Label(finestra, text="",fg="blue")
etiqueta3.pack()


canviar_text(etiqueta1, ask)
canviar_text(etiqueta2, askancel)
canviar_text(etiqueta3, sino)

finestra.mainloop()
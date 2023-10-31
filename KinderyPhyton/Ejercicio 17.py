import tkinter

def mostrar_seleccion():
    seleccion = pizza.get()
    resultado_label.config(text=f"Has seleccionado: {seleccion}")

finestra = tkinter.Tk()
ancho = 500
alto= 300
finestra.geometry(f"{ancho}x{alto}")

pizza = tkinter.StringVar()


INGREDIENTS = [
    ("Pernil", "pernil"),
    ("Ceba", "ceba"),
    ("Formatge", "formatge"),
    ("Piña", "piña")
]

for text_col1, text_col2 in INGREDIENTS:
    tkinter.Radiobutton(finestra, text=text_col1, variable=pizza, value=text_col1).pack()

seleccion = tkinter.Button(finestra, text="Muestra Selección", command=mostrar_seleccion)
seleccion.pack()

resultado_label = tkinter.Label(finestra, text="")
resultado_label.pack()

finestra.mainloop()
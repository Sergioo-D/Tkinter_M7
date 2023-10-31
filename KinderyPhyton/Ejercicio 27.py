import tkinter as tk

def mostrar_estat():
    valor = var.get()
    etiqueta.config(text=valor)

def desseleccionar():
    casella_seleccio.deselect()

finestra = tk.Tk()
finestra.title("Exemple de Casella de Selecció")

var = tk.StringVar()
var.set("estic seleccionada")

casella_seleccio = tk.Checkbutton(finestra, text="selecciona'm", variable=var, onvalue="estic seleccionada", offvalue="estic desseleccionada")
casella_seleccio.pack()

etiqueta = tk.Label(finestra, text=var.get())
etiqueta.pack()

boto_mostrar = tk.Button(finestra, text="Mostrar estat", command=mostrar_estat)
boto_mostrar.pack()

boto_desseleccionar = tk.Button(finestra, text="Desseleccionar", command=desseleccionar)
boto_desseleccionar.pack()

finestra.mainloop()
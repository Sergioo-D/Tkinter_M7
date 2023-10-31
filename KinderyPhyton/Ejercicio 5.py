import tkinter

finestra1 = tkinter.Tk()
finestra1.title("Ventana principal")

def accio():
    finestra2 = tkinter.Tk()
    finestra2.title("Ventana nueva")
    etiqueta = tkinter.Label(finestra2,text="El teu nom es: " + quadre_text.get())
    etiqueta.grid(row=2,column=2)


quadre_text = tkinter.Entry(finestra1)
boton = tkinter.Button(finestra1,text = "Pulsar", command=accio)
boton.grid(row=1,column=1)
quadre_text.grid(row=2,column=2)

finestra1.mainloop()
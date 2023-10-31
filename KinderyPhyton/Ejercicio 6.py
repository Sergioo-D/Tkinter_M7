import tkinter

finestra1 = tkinter.Tk()
finestra1.title("Ventana principal")
quadre_text = tkinter.Entry(finestra1)
quadre_text.insert(0,"Introdueix el teu nom")
quadre_text.grid(row=2,column=2)



def accio():
    finestra2 = tkinter.Tk()
    variable_text = "El teu nom es: " + quadre_text.get()
    finestra2.title("Ventana nueva")
    etiqueta = tkinter.Label(finestra2,text=variable_text)
    etiqueta.grid(row=2,column=2)



boton = tkinter.Button(finestra1,text = "Click per que et digui el teu nom", command=accio)
boton.grid(row=1,column=1)


finestra1.mainloop()
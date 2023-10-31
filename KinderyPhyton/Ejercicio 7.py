import tkinter

finestra = tkinter.Tk()
etiqueta = tkinter.Label(finestra,text="Hola buenas",bg="red",fg="green")
etiqueta.grid(row=1,column=1)

boton = tkinter.Button(finestra,text="Pulsame",fg="blue",bg="yellow")
boton.grid(row=1,column=2)
finestra.mainloop()
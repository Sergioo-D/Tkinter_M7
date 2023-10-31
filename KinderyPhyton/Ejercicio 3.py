import tkinter

finestra = tkinter.Tk()

etiqueta1 = tkinter.Label(finestra, text= "Segundo")
etiqueta1.grid(row= 1,column=2)

etiqueta2 = tkinter.Label(finestra, text= "Primero")
etiqueta2.grid(row= 1, column=1)

etiqueta3= tkinter.Label(finestra, text= "Tercero")
etiqueta3.grid(row = 1,column =3)

boton =tkinter.Button(finestra, text="Aceptar",state= tkinter.NORMAL,padx = 4,pady=4)
boton.grid(row = 2, column = 2)
finestra.mainloop()
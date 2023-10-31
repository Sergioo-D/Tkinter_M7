import tkinter

finestra = tkinter.Tk()

etiqueta1 = tkinter.Label(finestra, text= "Segundo")
etiqueta1.grid(row= 1,column=2)

etiqueta2 = tkinter.Label(finestra, text= "Primero")
etiqueta2.grid(row= 1, column=1)

etiqueta3= tkinter.Label(finestra, text= "Tercero")
etiqueta3.grid(rowspan = 1,column =3)

finestra.mainloop()
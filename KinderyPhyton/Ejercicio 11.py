import tkinter

finestra = tkinter.Tk()

finestra.iconbitmap("logo01.ico")

boton_quit = tkinter.Button(finestra,command=finestra.quit,text="Cerrar")
boton_quit.grid(row=1,column=1)

finestra.mainloop()
import tkinter



def botonActualizado():

    if interruptor.get() == 1:
        boton_adelante.config(state=tkinter.NORMAL)
    else:
        boton_adelante.config(state=tkinter.DISABLED)

def palante():
    print("Has pulsado adelante")


finestra = tkinter.Tk()
finestra.title("Radio Button")
ancho= 300
alto = 300
finestra.geometry(f"{ancho}x{alto}")

interruptor = tkinter.IntVar()
interruptor.set(0)

boton_declino = tkinter.Radiobutton(finestra,text="Declinar",command=botonActualizado,variable=interruptor,value=2)
boton_declino.pack()
boton_acepto =tkinter.Radiobutton (finestra,text="Acceptar",command=botonActualizado,variable=interruptor,value=1)
boton_acepto.pack()


boton_adelante = tkinter.Button(finestra,text="Endevant",state= tkinter.DISABLED,command=palante)
boton_adelante.pack()






finestra.mainloop()
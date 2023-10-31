import tkinter

def crear_tk():
    nuevaTK = tkinter.Tk()
    ancho= 200
    largo= 200
    nuevaTK.geometry(f"{ancho}x{largo}")
    etiqueta = tkinter.Label(nuevaTK,text="Soy una TK")
    etiqueta.pack()
    cerrar = tkinter.Button(nuevaTK,text="Cerrar", command= nuevaTK.destroy)
    cerrar.pack()

def top_level():
    nuevaTopLevel = tkinter.Toplevel()
    ancho= 200
    largo= 200
    nuevaTopLevel.geometry(f"{ancho}x{largo}")
    etiqueta = tkinter.Label(nuevaTopLevel,text="Soy una TopLevel")
    etiqueta.pack()
    cerrar = tkinter.Button(nuevaTopLevel,text="Cerrar", command= nuevaTopLevel.destroy)
    cerrar.pack()


principal = tkinter.Tk()
ancho = 400
largo = 200
principal.geometry(f"{ancho}x{largo}")

botonTk = tkinter.Button(principal,text="Creacion TK",command=crear_tk)
botonTk.pack()
botonTop= tkinter.Button(principal,text="Creacion TopLevel", command=top_level)
botonTop.pack()



principal.mainloop()
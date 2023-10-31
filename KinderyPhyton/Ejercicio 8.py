import tkinter


def click_boto(number):
    quadre_text.insert(tkinter.END, str(number))

def borrar():
    quadre_text.delete(0,tkinter.END)


finestra = tkinter.Tk()
finestra.title("Teclado Numérico")

quadre_text = tkinter.Entry(finestra)
quadre_text.grid(row=0, column=0, columnspan=4)

for i in range(10):
    boton = tkinter.Button(finestra, text=str(i), command=lambda i=i: click_boto(i))
    boton.grid(row=(i // 3) + 3, column=(i % 3))

boton_borra = tkinter.Button(finestra,text="DEL",command=lambda :borrar())
boton_borra.grid(row=8,column=1)

finestra.mainloop()


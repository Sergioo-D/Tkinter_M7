import tkinter

def click_boto(number):
    quadre_text.insert(tkinter.END, str(number))

def borrar():
    quadre_text.delete(0, tkinter.END)

def borrar_ultimo_numero():
    texto_actual = quadre_text.get()
    if texto_actual:
        nuevo_texto = texto_actual[:-1]
        quadre_text.delete(0, tkinter.END)
        quadre_text.insert(0, nuevo_texto)


def operaciones(operacion):
    texto_actual = quadre_text.get()

    if '+' in texto_actual:
        numeros = texto_actual.split("+")
        if len(numeros) == 2:
            num1 = int(numeros[0])
            num2 = int(numeros[1])
            resultado = num1 + num2
            quadre_text.delete(0, tkinter.END)
            quadre_text.insert(tkinter.END, str(resultado))

def igual():
    operaciones("+")

finestra = tkinter.Tk()
finestra.title("Teclado Numérico")

quadre_text = tkinter.Entry(finestra)
quadre_text.grid(row=0, column=0, columnspan=3)

button_labels = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0","+"]

for i, label in enumerate(button_labels):
    boton = tkinter.Button(finestra, text=label, command=lambda label=label: click_boto(label))
    boton.grid(row=i // 3 + 1, column=i % 3)

boton_borra = tkinter.Button(finestra, text="CLEAR", command=borrar)
boton_borra.grid(row=5, column=1)

boton_borrar_ultimo = tkinter.Button(finestra, text="DEL", command=borrar_ultimo_numero)
boton_borrar_ultimo.grid(row=5, column=0)


boton_igual = tkinter.Button(finestra, text="=", command=igual)
boton_igual.grid(row=6, column=2)

finestra.mainloop()
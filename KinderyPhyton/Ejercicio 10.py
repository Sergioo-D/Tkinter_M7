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

    if "+" in texto_actual:
        numeros = texto_actual.split("+")
        if len(numeros) == 2:
            num1 = float(numeros[0])
            num2 = float(numeros[1])
            resultado = num1 + num2
            quadre_text.delete(0, tkinter.END)
            quadre_text.insert(tkinter.END, str(resultado))
    elif "-" in texto_actual:
        numeros = texto_actual.split("-")
        if len(numeros) == 2:
            num1 = float(numeros[0])
            num2 = float(numeros[1])
            resultado = num1 - num2
            quadre_text.delete(0, tkinter.END)
            quadre_text.insert(tkinter.END, str(resultado))
    elif "*" in texto_actual:
        numeros = texto_actual.split("*")
        if len(numeros) == 2:
            num1 = float(numeros[0])
            num2 = float(numeros[1])
            resultado = num1 * num2
            quadre_text.delete(0, tkinter.END)
            quadre_text.insert(tkinter.END, str(resultado))
    elif "/" in texto_actual:
        numeros = texto_actual.split("/")
        if len(numeros) == 2:
            num1 = float(numeros[0])
            num2 = float(numeros[1])
            if num2 != 0:
                resultado = num1 / num2
                quadre_text.delete(0, tkinter.END)
                quadre_text.insert(tkinter.END, str(resultado))
            else:
                quadre_text.delete(0, tkinter.END)
                quadre_text.insert(tkinter.END, "Error")

def igual():
    operaciones("+")
    operaciones("-")
    operaciones("*")
    operaciones("/")

finestra = tkinter.Tk()
finestra.title("Calculadora")

quadre_text = tkinter.Entry(finestra)
quadre_text.grid(row=0, column=0, columnspan=4)

button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0",  "+"
]

row_num = 1
col_num = 0

for label in button_labels:
    boton = tkinter.Button(finestra, text=label, width=5, height=2, command=lambda label=label: click_boto(label))
    boton.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

boton_igual = tkinter.Button(finestra, text="=", width=5, height=2, command=igual)
boton_igual.grid(row=row_num, column=col_num, padx=5, pady=5)

boton_borra = tkinter.Button(finestra, text="CLEAR", command=borrar)
boton_borra.grid(row=5, column=1)

boton_borrar_ultimo = tkinter.Button(finestra, text="DEL", command=borrar_ultimo_numero)
boton_borrar_ultimo.grid(row=5, column=0)

finestra.mainloop()
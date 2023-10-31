import tkinter as tk

def actualizar_etiqueta():
    valor1 = b_lliscan1.get()
    valor2 = b_lliscan2.get()
    etiqueta.config(text=f"Valor del botón lliscante 1: {valor1}\nValor del botón lliscante 2: {valor2}")

finestra = tk.Tk()
ancho = 400
largo = 400
A = finestra.winfo_screenwidth()
B = finestra.winfo_screenheight()
eje_x = (A - ancho) // 2
eje_y = (B - largo) // 2
finestra.geometry(f"{ancho}x{largo}+{eje_x}+{eje_y}")

b_lliscan1 = tk.Scale(from_=10, to=50)
b_lliscan1.grid(padx=5, pady=5, column=1, rowspan=4, sticky="ne")

b_lliscan2 = tk.Scale(orient="horizontal", from_=10, to=50)
b_lliscan2.grid(padx=5, pady=5, column=2, rowspan=4, sticky="ne")

boto_1 = tk.Button(finestra, text="Actualizar etiqueta", command=actualizar_etiqueta)
boto_1.grid(padx=5, pady=5, column=3, row=0)

boto_2 = tk.Button(finestra, text="Actualizar etiqueta", command=actualizar_etiqueta)
boto_2.grid(padx=5, pady=5, column=3, row=1)

etiqueta = tk.Label(finestra, text="")
etiqueta.grid(padx=5, pady=5, column=4, row=0, rowspan=2)

finestra.mainloop()
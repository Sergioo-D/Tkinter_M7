import os
import sqlite3
import tkinter
from tkinter import messagebox


def crear_BD():
    try:
        if not os.path.exists("./bd"):
            os.makedirs('bd')
        laBD = sqlite3.connect('bd/basquet.db')
        cur_BD = laBD.cursor()
        cur_BD.execute('''
                       CREATE TABLE IF NOT EXISTS jugadors (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nom TEXT NOT NULL,
                           cognom TEXT NOT NULL,
                           alçada FLOAT, 
                           edat INTEGER
                       )''')
        print("Tabla creada o ya existe")

        laBD.commit()
        laBD.close()
    except sqlite3.Error as error:
        print("Error al crear la tabla:", error)

    if __name__ == "__main__":
        connect_db()


#----------------------------------------------------------------------------------------------

def connect_db():
    try:

        var_BD= sqlite3.connect("./bd/basquet.db")
        cur_BD = var_BD.cursor()
        cur_BD.execute("SELECT * from jugadors")
        var_dades = cur_BD.fetchall()

        print("Contingut de la base de dades:")
        for row in var_dades:
            print(row)
        var_BD.close()
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"Ha ocorregut un error: {error}")


def registarJugadores():
    try:
        crear_BD()
        laBd = sqlite3.connect("./bd/basquet.db")
        cur_BD = laBd.cursor()
        nom = entradaNom.get()
        cognom = entradaCognom.get()
        alçada = entradaAlçada.get()
        edat = entradaEdat.get()

        cur_BD.execute("INSERT INTO jugadors (nom, cognom, alçada, edat) VALUES (?, ?, ?, ?)",
                       (nom, cognom, alçada, edat))

        laBd.commit()
        laBd.close()
        messagebox.showinfo("info", "Jugador registrado exitosamente")
    except sqlite3.Error as error:
        messagebox.showerror("Error", f"Ha ocurrido un error: {error}")


finestra = tkinter.Tk()
finestra.title("BBDD Basquet")
ancho = 400
largo = 400
A = finestra.winfo_screenwidth()
B = finestra.winfo_screenheight()
eje_x = (A - ancho) // 2
eje_y = (B - largo) // 2
finestra.geometry(f"{ancho}x{largo}+{eje_x}+{eje_y}")


labelNom = tkinter.Label(finestra, text="Nom:")
labelNom.grid(row=0, column=0)
labelCognom = tkinter.Label(finestra, text="Cognom:")
labelCognom.grid(row=1, column=0)
labelAlçada = tkinter.Label(finestra, text="Alçada:")
labelAlçada.grid(row=2, column=0)
labelEdat = tkinter.Label(finestra, text="Edat:")
labelEdat.grid(row=3, column=0)

entradaNom = tkinter.Entry(finestra)
entradaNom.grid(row=0, column=1)
entradaCognom = tkinter.Entry(finestra)
entradaCognom.grid(row=1, column=1)
entradaAlçada = tkinter.Entry(finestra)
entradaAlçada.grid(row=2, column=1)
entradaEdat = tkinter.Entry(finestra)
entradaEdat.grid(row=3, column=1)


botonRegistar = tkinter.Button(finestra,text="Registrar Jugador",command=registarJugadores)
botonRegistar.grid(row=4, column=0, columnspan=2)

botonConectar = tkinter.Button(finestra, text="Print datos", command=connect_db)
botonConectar.grid(row=5,column=0,columnspan=2)


finestra.mainloop()
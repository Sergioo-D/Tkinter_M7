import tkinter
from tkinter import messagebox

def showinfo() :
    messagebox.showinfo("message box", "Hola buenas tardes")

def showwarning():
    messagebox.showwarning("Prueba", "Holaaaa")

def showerror():
    messagebox.showerror("Prueba", "Holaaaa")

def askquestion():
    messagebox.askquestion("Prueba", "Holaaaa")

def askokcancel():
    messagebox.askokcancel("Prueba", "Holaaaa")

def askyesno():
    messagebox.askyesno("Prueba", "Holaaaa")

showwarning()
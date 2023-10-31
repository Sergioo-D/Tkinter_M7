import tkinter
from PIL import ImageTk, Image

finestra = tkinter.Tk()

imagen= ImageTk.PhotoImage(Image.open("./foto/cr7.png"))

imagen_label = tkinter.Label(finestra,image=imagen)
imagen_label.pack()

finestra.mainloop()
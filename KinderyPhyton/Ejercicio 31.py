import sqlite3
import os


def crear_BD():
   try:
       if not os.path.exists("./bd"):
           os.makedirs('bd')
       laBD = sqlite3.connect('bd/basquet.db')
       cur_BD = laBD.cursor()

       cur_BD.execute('''CREATE TABLE jugadors (
                                       nom TEXT, 
                                       cognom TEXT, 
                                       alçada REAL, 
                                       edat INTEGER
                                   )''')
       print("Tabla creada correctamente")

       laBD.commit()
       laBD.close()
   except sqlite3.Error as error:
       print("Error al crear la tabla, ya esxiste tabla jugadors")

if __name__ == '__main__':
   crear_BD()
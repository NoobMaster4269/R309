from tkinter import *

fenetre = Tk()

frame2 = Frame(fenetre)
        frame2.pack(padx = 10, pady = 10)

        frame2.destroy()

        mes = Entry(frame2)
        mes.grid(row = 0, column = 0, padx = 5)
from tkinter import *
from random import randint



fenetre = Tk()
fenetre.geometry("400x400")

label = Label(fenetre, text = "caca")
label.pack()

frame = Frame()

text = Text(fenetre)


entree = Entry(fenetre)
entree.pack()
i = 0
def saisie():
    text.insert(INSERT, entree.get() + "\n")
    entree.delete(0, END)

def saisie2():
    text.delete("1.0", "end")
    

bou1 = Button(fenetre, text = 'valider', command = saisie)
bou2 = Button(fenetre, text = 'valider2', command = saisie2)
bou2.pack()
bou1.pack()
text.pack()
fenetre.mainloop()




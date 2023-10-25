from tkinter import *
from random import randint



fen1 = Tk()
 
entree = Entry(fen1)#demande la valeur
entree.pack() # integration du widget a la fenetre principale
def saisie():
    label = Label(fen1, text = entree.get())
    label.pack()


bou1 = Button(fen1, text = 'valider', command = saisie)
bou1.pack()
bou2 = Button(fen1, text = "quitter", command = fen1.destroy)
bou2.pack()
fen1.mainloop()
print (saisie)


text = Entry(fenetre)
topic = Label(fenetre, text = "Topic")
topic.pack()
text.pack()
def saisie():
    label = Label(fenetre, text = entree.get())
    label.pack()
bou1 = Button(fenetre, text = 'valider', command = saisie)
bou1.pack()
bou2 = Button(fenetre, text = "quitter", command = fenetre.destroy)
bou2.pack()
from tkinter import *

# Créez la fenêtre principale
fenetre = Tk()
fenetre.title("Exemple de séparation de widgets")
fenetre.geometry("400x400")
# Créez un cadre pour les widgets en haut
frame_top = Frame(fenetre)
frame_top.pack(padx=10, pady=5)

# Ajoutez des boutons, une entrée et une zone de texte dans le cadre du haut
button1 = Button(frame_top, text="Bouton 1")
button2 = Button(frame_top, text="Bouton 2")
entry1 = Entry(frame_top)
text_widget = Text(frame_top, height=5, width=50)

button1.grid(row=0, column=0, padx=5)
button2.grid(row=0, column=1, padx=5)
entry1.grid(row=1, column=0, padx=5)
text_widget.grid(row=2, column=0, columnspan=2, padx=0, pady= 5)

# Créez un cadre pour les widgets en bas
frame_bottom = Frame(fenetre)
frame_bottom.pack(padx=10, pady=20)

# Ajoutez une entrée et un bouton dans le cadre du bas
entry2 = Entry(frame_bottom)
button3 = Button(frame_bottom, text="Bouton 3")

entry2.grid(row=0, column=0, padx=5)
button3.grid(row=0, column=1, padx=5)

# Lancement de la boucle principale tkinter
fenetre.mainloop()
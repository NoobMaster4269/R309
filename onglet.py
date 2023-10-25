import tkinter as tk                    
from tkinter import ttk
  
  
fenetre = tk.Tk()
fenetre.geometry("400x400")
fenetre.title("Tab Widget")
tabControl = ttk.Notebook(fenetre)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Topic 1')
tabControl.add(tab2, text ='Topic 2')
tabControl.pack(expand = 1, fill ="both")
  

fenetre.mainloop()
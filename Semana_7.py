# Gui - grafical use interfaces
# 
# Tkinter - funcionalidades de desenvolvimento de interfaces gráficas

from tkinter import Tk, Label, PhotoImage

root = Tk()
photo = PhotoImage (file = "gato.gif").subsample(5)
hello = Label(master= root, image=photo, width = 300, height= 180)
hello.pack()
root.mainloop()

root = Tk()
hello = Label (master=root, text = "Bom dia!")
hello.pack()
root.mainloop()
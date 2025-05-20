# Gui - grafical use interfaces
# 
# Tkinter - funcionalidades de desenvolvimento de interfaces gráficas

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage (file = "gato.gif").subsample(5)
hello = Label(master= root, image=photo, width = 300, height= 180)
hello.pack()
root.mainloop()

root = Tk()
hello = Label (master=root, text = "Bom dia!")
hello.pack()
root.mainloop()

# Interfaces Gráficas
# A posiçao dos componentes na janela pe gerenciada pelo geometry manager da tkinter
# O método pack é uma forma de forneceer estas diretivas ao sistema

root = Tk()
photo = PhotoImage (file = "gato.gif").subsample(5)
image = Label(master= root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=('Courier', 18), text='Olá, pessoal!')
text.pack(side=BOTTOM)
root.mainloop()

# Side: especifica o lugar onde o objeto será inserido
# Grid(): transforma a janela em uma matriz de linhas e colunas
# a partir de então, se escolhe qual célula armazenar um widget. 

# Exercício

from tkinter import Tk, Label, RAISED
root = Tk()
labels = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
    ["*","0","#"]
]
for r in range (4):
    for c in range(3):
        label= Label(root, relief=RAISED, padx=10, text=labels[r][c])
        label.grid(row=r,column=c)
        
root.mainloop()

# Programação orientada a eventos
# Cada evento é uma ação do usuário e cada evento leva a uma tarefa que será executada pleo programa
# mainloop() função que faz com que uma janela seja exibida na tela

# Exemplo 1
from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime("Day:%d %b %Y\nTime: %H:%M:%S%p\n",localtime())
    showinfo(message=time)

root = Tk()
button = Button(root, text="clique", command=clicked)
button.pack()
root.mainloop()

# Exemplo 2
from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def clicked():
    global entry
    data = entry.get()
    weekday = strftime("%A", strptime(date,"%b %d, %Y"))
    time = strftime("Day:%d %b %Y\nTime: %H:%M:%S%p\n",localtime())
    showinfo(message = '{} was a {}'.format(date,weekday))

root = Tk()
label = Label (root, text = "Digite uma data:")
label.grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
button = Button(root, text= 'Clique', command=clicked)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()


from tkinter import Tk, Button, Label, Entry, END 
 
def clicked(): 
    global entry 
    name = entry.get() 
    print('Ola', name) 
    entry.delete(0, END) 
 
root = Tk() 
label = Label(root, text='Nome:') 
label.grid(row=0, column=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
button = Button(root, text='OK', command=clicked) 
button.grid(row=1, column=0, columnspan=2) 
root.mainloop() 


from tkinter import Tk, Button, Label, Entry, END 
 
def clicked(): 
    global entry 
    name = entry.get() 
    print('Ola', name) 
    entry.delete(0, END) 
 
root = Tk() 
label = Label(root, text='Nome:') 
label.grid(row=0, column=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
button = Button(root, text='OK', command=clicked) 
button.grid(row=1, column=0, columnspan=2) 
root.mainloop() 





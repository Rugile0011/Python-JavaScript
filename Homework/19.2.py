from tkinter import *

window = Tk()
saved = StringVar()

def printing(event):
    input = input.get()
    saved.set(input)
    result['text'] = f'Labas,{input} !'


note = Label(window, text="Iveskite vardą")
entry = Entry(window)
button = Button(window, text='Patvirtinti', fg="white", bg="pink", command=printing)
window.bind('<Return>', lambda event: printing())
result = Label(window, text="")

button.bind("<Button-1>", printing)
window.bind("<Return>", printing)

note.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
result.grid(row=1, columnspan=3)


my_menu = Menu(window)
window.config(menu=my_menu)
submeniu = Menu(meniu, tearoff=0)

def isvalyti():
    result['text']=''
def atkurti_paskutini():
    result['text'] = f'Labas,{saved.get()}!'
def uzdaryti():
    window.destroy()

my_menu.add_cascade(labe="Meniu", menu=submenu)
submenu.add_command(label="Išvalyti", command=isvalyti)
submenu.add_command(label="Atkurti paskutinį", command=atkurti_paskutini)
submenu.add_separator()
submenu.add_command(label="Išeiti", command=uzdaryti)


window.mainloop()

from tkinter import *

langas = Tk()
issaugota = StringVar()
langas.geometry('300x80')

def spausdinti(event):
    ivesta = ivesti.get()
    issaugota.set(ivesta)
    rezultatas['text'] = f'Labas,{ivesta} !'


uzrasas = Label(langas, text="Iveskite vardą")
ivesti = Entry(langas)
mygtukas = Button(langas, text='Patvirtinti', fg="white", bg="pink", command=spausdinti)
langas.bind('<Return>', lambda event: spausdinti())
rezultatas = Label(langas, text="")

mygtukas.bind("<Button-1>", spausdinti)
langas.bind("<Return>", spausdinti)

uzrasas.grid(row=0, column=0)
ivesti.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)


meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

def isvalyti():
    rezultatas['text']=''
def atkurti_paskutini():
    rezultatas['text'] = f'Labas,{issaugota.get()}!'
def uzdaryti():
    langas.destroy()

meniu.add_cascade(labe="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti paskutinį", command=atkurti_paskutini)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=uzdaryti)


statusbar = Label(langas, text="on the way…", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

#Nerandu klaidos

langas.mainloop()

from tkinter import *

langas = Tk()

def spausdinti(event):
    ivesta = laukas.get()
    rezultatas["text"] = "Labas," + ivesta + "!"


mygtukas = Button(langas, text="Patvirtinti", fg="white", bg="pink")
uzrasas = Label(langas, text="Iveskite vardą")
laukas = Entry(langas)
rezultatas = Label(langas, text="")

mygtukas.bind("<Button-1>", spausdinti)
langas.bind("<Return>", spausdinti)

uzrasas.grid(row=0, column=0)
laukas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)


langas.mainloop()

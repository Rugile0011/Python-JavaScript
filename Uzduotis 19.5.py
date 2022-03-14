import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=150)
canvas.pack()


def leapyear():
    year = int(entry.get())
    if year % 4 == 0 and year % 100 != 0:
        answer1 = tk.Label(root, text=('{} is leap year'.format(year))).place(x=105, y=120)
    else:
        answer2 = tk.Label(root, text=('{} is not leap year'.format(year))).place(x=105, y=120)


label = tk.Label(root, text="Input Year").place(x=50, y=50)
entry = tk.Entry(root)
canvas.create_window(190, 62, window=entry)
button = tk.Button(root, text="Check", command=leapyear).place(x=130, y=85)

root.mainloop()

import tkinter as tk
from tkinter import *
gui = tk.Tk()
gui.title('Python')
gui.geometry('800x400')
gui.configure(bg='#856ff8') # COLOR

gui.attributes("-fullscreen", 0.9)


def Camera():
    print("Iqbal is our mentor")


button1 = Button(gui, text = "First Practice", font=('Times', '18', 'bold italic'), borderwidth=10, highlightthickness=4, highlightbackground="green",relief=SUNKEN,command=Camera)

button1.configure(width=15, activebackground = "white")

button1.place(x=180, y=100)


gui.mainloop()

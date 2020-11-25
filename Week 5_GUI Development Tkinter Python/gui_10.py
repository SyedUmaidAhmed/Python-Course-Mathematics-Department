import tkinter as tk
from tkinter import *
gui = tk.Tk()
gui.title('Python')
gui.geometry('800x400')
gui.configure(bg='#856ff8') # COLOR

gui.attributes("-fullscreen", 0.9)


def Camera():
    print("Iqbal is our mentor")



textual = Label(gui, text= "GUI Development System", font=('Times New Roman', '35', 'bold'), bg='#856ff8', fg='green')
textual.pack()


E1 = Entry(gui, width=40, bd=5)
#E1.pack()
#E1.place(x = 300, y = 180,width=200,height=100)


# For padx and pady in Entry please Explore

#https://www.delftstack.com/howto/python-tkinter/how-to-set-height-and-width-of-tkinter-entry-widget/



button1 = Button(gui, text = "First Practice", font=('Times', '18', 'bold italic'), borderwidth=10, highlightthickness=4, highlightbackground="green",relief=SUNKEN,command=Camera)

button1.configure(width=15, activebackground = "white")

button1.place(x=180, y=100)


gui.mainloop()

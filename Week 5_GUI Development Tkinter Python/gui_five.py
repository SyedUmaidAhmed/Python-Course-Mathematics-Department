import tkinter as tk

def change():
    my_string_var.set('Second Time')

root = tk.Tk()
root.title('Mathematics')
root.geometry('300x150')
my_string_var = tk.StringVar()
my_string_var.set('First Time')
tk.Label(root, textvariable=my_string_var).grid()
tk.Button(root, text='Change', command=change).grid(row=1)
root.mainloop()

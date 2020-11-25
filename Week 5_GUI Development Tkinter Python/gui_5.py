import tkinter as tk
gui = tk.Tk()

gui.title('Python')
#gui.geometry('800x400')

gui.configure(bg='#856ff8') # COLOR

gui.geometry("{0}x{1}+0+0".format(gui.winfo_screenwidth(), gui.winfo_screenheight()))

#gui.attributes("-fullscreen", True)  #FULL SCREEN

gui.mainloop()

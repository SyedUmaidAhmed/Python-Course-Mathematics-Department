from tkinter import *

top=Tk()

top.geometry('800x400')  #SIZE

def Button_backend():

    print("Your Button is working Fine")


B = Button(top,text="Mathematics",command=Button_backend)

B.place(x=300,y=100)

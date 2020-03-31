from tkinter import *

top=Tk()

top.geometry('800x400')  #SIZE

def Button_backend():

    print("Your Button is working Fine")


B = Button(top,text="Mathematics",command=Button_backend)

B.place(x=300,y=100)


B1 = Button(top,text="Mathematics one",command=Button_backend)

B1.place(x=300,y=200)


B2 = Button(top,text="Mathematics two",command=Button_backend)

B2.place(x=300,y=300)


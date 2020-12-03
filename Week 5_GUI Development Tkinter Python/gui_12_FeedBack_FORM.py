import tkinter
from tkinter import *
def save():
    text=E1.get()+"\n"+E2.get()+"\n"+E3.get()+"\n"+E4.get()+"\n"+E5.get()+"\n"+E6.get()+"\n"+E7.get()+"\n"+E8.get()+"\n"+E9.get()
    with open ("text.txt",'w')as f:
        f.writelines(text)

nimrah=tkinter.Tk()
nimrah.title("nimrah ansari")
nimrah.geometry('675x590')
title=Label(nimrah,text="STUDENT INFORMATION",font=("areil 20 bold italic "),fg="lightblue").grid(row=0,column=2)


line1=Label(nimrah,text="STUDENT NAME:",font=("Arial 12 bold italic  ")).grid(row=1, column=1, padx=20, sticky='w')
E1=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E1.grid(row=1,column=2,pady=10,padx=20,sticky="e")

line2=Label(nimrah,text="FATHER NAME:",font=("Arial 12 bold  ")).grid(row=2, column=1, padx=20, sticky='w')
E2=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E2.grid(row=2,column=2,pady=10,padx=20,sticky="e")

line3=Label(nimrah,text="SEAT NUMBER:",font=("Arial 12 bold italic ")).grid(row=3, column=1, padx=20, sticky='w')
E3=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E3.grid(row=3,column=2,pady=10,padx=20,sticky="e")

line4=Label(nimrah,text="SECTION:",font=("Arial 12 bold italic ")).grid(row=4,column=1, padx=20, sticky='w')
E4=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E4.grid(row=4,column=2,pady=10,padx=20,sticky="e")

line5=Label(nimrah,text="DEPARTMENT:",font=("Arial 12 bold italic ")).grid(row=5, column=1, padx=20, sticky='w')
E5=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E5.grid(row=5,column=2,pady=10,padx=20,sticky="e")

line6=Label(nimrah,text="SUBJECT:",font=("Arial 12 bold italic ")).grid(row=6, column=1, padx=20, sticky='w')
E6=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E6.grid(row=6,column=2,pady=10,padx=20,sticky="e")

line7=Label(nimrah,text="DATE OF BIRTH:",font=("Arial 12 bold italic ")).grid(row=7, column=1, padx=20, sticky='w')
E7=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E7.grid(row=7,column=2,pady=10,padx=20,sticky="e")

line8=Label(nimrah,text="PHONE NUMBER:",font=("Arial 12 bold italic ")).grid(row=8, column=1, padx=20, sticky='w')
E8=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E8.grid(row=8,column=2,pady=10,padx=20,sticky="e")

line9=Label(nimrah,text="EMAIL ADDRESS:",font=("Arial 12 bold italic ")).grid(row=9, column=1, padx=20, sticky='w')
E9=Entry(nimrah,bd=5,relief=GROOVE,width=60)
E9.grid(row=9,column=2,pady=10,padx=20,sticky="e")



# to save enter data in txt file
button_quit=Button(nimrah,text="OK",command=save,width=12,height=2,bg="lightblue")
button_quit.grid(row=10,column=2, pady=10)
# to close window
button_quit_1=Button(nimrah,text="Cancel",command=nimrah.destroy,width=12,height=2,bg="lightblue")
button_quit_1.grid(row=12,column=2)

nimrah.mainloop()

import tkinter
from tkinter import*
from tkinter import messagebox

m=tkinter.Tk()
m.title('Online Booking Of Movie Tickets')
m.geometry('500x500')

l_select=None

def submit():
    if(l_select==None):
        messagebox.showinfo("Error")
    else:
        messagebox.showinfo('Message','Successful')

def sel():
    global l_select
    l_select=str(v.get())
    

head_l=Label(m,text='Online Booking Of Movie Tickets',font=("Times", 15, "bold"))
head_l.pack()

lang_l=Label(m,text='Select Language',font=("Times",10,"bold"))
lang_l.pack(anchor=W)
v = IntVar() 
Radiobutton(m, text='Kannada', variable=v, value=1,command=sel).pack(anchor=W) 
Radiobutton(m, text='English', variable=v, value=2,command=sel).pack(anchor=W)
Radiobutton(m, text='Hindi', variable=v, value=3,command=sel).pack(anchor=W)


mov_l=Label(m,text='Select Movie',font=("Times",10,"bold"))
mov_l.pack(anchor=W) 
var1 = IntVar() 
Checkbutton(m, text='X', variable=var1).pack(anchor=W) 
var2 = IntVar() 
Checkbutton(m, text='Y', variable=var2).pack(anchor=W)

tic_l=Label(m,text='Select no. of Tickets',font=("Times",10,"bold"))
tic_l.pack(anchor=W)
w = Spinbox(m, from_ = 1, to = 10) 
w.pack(anchor=W) 

button=Button(m,text='SUBMIT',width=25,command=submit)
button.pack()

m.mainloop()

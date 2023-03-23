from tkinter import *

screen = Tk()
screen.geometry("500x500")

var_name = StringVar()
var_email = StringVar()

def myfun():
    f=open('records.txt','a')
    f.write("\n ------------------------------\n")
    f.write("\n name = "+var_name.get())
    f.write("\n email = "+var_email.get())
    var_name.set("")
    var_email.set("")
    f.close()

lbl=Label(screen,text="User Details",font=('arial',26,'bold'))
lbl.place(x=150,y=20)

lbl_name=Label(screen,text="Enter your name : ",font=('arial',16,'bold'))
lbl_name.place(x=20,y=150)

e_name=Entry(screen,width=25,textvariable=var_name)
e_name.place(x=220,y=160)

lbl_email=Label(screen,text="Enter your email : ",font=('arial',16,'bold'))
lbl_email.place(x=20,y=180)

e_email=Entry(screen,width=25,textvariable=var_email)
e_email.place(x=220,y=190)

btn=Button(screen,text="Submit",font=('arial',16,'bold'),bg="blue",fg="white",command=myfun)
btn.place(x=260,y=250)

screen.mainloop()
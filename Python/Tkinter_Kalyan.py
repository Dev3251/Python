from tkinter import *

screen = Tk()
screen.title("KALYAN JEWELLERS")
screen.geometry("1000x600")
screen.configure(background="khaki")

lbl = Label(screen,text="** WELCOME TO KALYAN JEWELLERS **",font=('arial',25,'bold','underline'),foreground="crimson",background="khaki")
lbl.place(x=140,y=10)

lbl_details=Label(screen,text="User Details -->",font=('arial',20,'bold','underline'),fg="blue",bg="khaki")
lbl_details.place(x=50,y=80)

lbl_name=Label(screen,text="Enter your name : ",font=('arial',15,'bold'),fg="blue",bg="khaki")
lbl_name.place(x=50,y=150)

e_name=Entry(screen,width=25)
e_name.place(x=240,y=157)

screen.mainloop()
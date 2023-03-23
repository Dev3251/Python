from tkinter import *

screen = Tk()
screen.title("Amaze Pizza")
screen.geometry("1000x600")
screen.configure(background="khaki")
var1=StringVar()
var2=StringVar()
var3=StringVar()

def menu():
    var1.set("1. large pizza = 10.99 AUD\n 2. large pizzas = 20.99 AUD \n3. large pizzas = 29.99 AUD\n4. large pasta = 9.5 AUD\n 5. large pastas = 17.00 AUD\n 6. large pastas = 27.50 AUD")

def offer():
    var2.set("1.Buy 4 or more pizza and get 1.5lt of soft drink free\n2.Buy 4 or more pastas and get 2 bruschetta free\n3.Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.")

    

lbl_head=Label(screen,text="*** WELCOME TO AMAZE PIZZA ****",font=('arial',40,'bold'),foreground="red",background="khaki")
lbl_head.place(x=50,y=20)

btn_menu=Button(screen,text="VIEW MENU",font=('arial',20,'bold'),foreground="cyan",background="blue",command=menu)
btn_menu.place(x=50,y=120)

lbl_menu=Label(screen,textvariable=var1,font=('arial',20,'bold'),foreground="red",background="khaki")
lbl_menu.place(x=50,y=200)

btn_offer=Button(screen,text="OFFERS",font=('arial',20,'bold'),foreground="cyan",background="blue",command=offer)
btn_offer.place(x=50,y=420)

lbl_offer=Label(screen,textvariable=var2,font=('arial',20,'bold'),foreground="red",background="khaki")
lbl_offer.place(x=50,y=490)

btn_order=Button(screen,text="ORDER NOW",font=('arial',20,'bold'),foreground="cyan",background="blue")
btn_order.place(x=500,y=650)

lbl_name=Label(screen,text="Enter your name : ",font=('arial',16,'bold'))
lbl_name.place(x=600,y=150)

e_name=Entry(screen,width=25)
# e_name.place(x=220,y=160)

lbl_pizza=Label(screen,text="Number of Pizzas You want : ",font=('arial',16,'bold'))
lbl_pizza.place(x=600,y=220)

e_pizza=Entry(screen,width=25)
# e_pizza.place(x=220,y=160)

lbl_pasta=Label(screen,text="Number of Pastas You want : ",font=('arial',16,'bold'))
lbl_pasta.place(x=600,y=290)

e_pasta=Entry(screen,width=25)
# e_pasta.place(x=220,y=160)


screen.mainloop()
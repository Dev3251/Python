import tkinter
import random

screen = tkinter.Tk()
screen.title("STONE PAPER SCISSOR")
screen.geometry("700x500")
screen.configure(background="khaki")

var1=tkinter.StringVar()
var2=tkinter.StringVar()
var3=tkinter.IntVar()
var4=tkinter.IntVar()
var5=tkinter.StringVar()
l=['ROCK','PAPER','SCISSOR']
u_count=0
c_count=0

def main_fun1(var1,var2):
    global u_count 
    global c_count
    if (var1=="PAPER" and var2=="ROCK") or (var1=="SCISSOR" and var2=="PAPER") or (var1=="ROCK" and var2=="SCISSOR"):
        u_count+=1  
        var5.set("You win")
    elif(var2=="PAPER" and var1=="ROCK") or (var2=="SCISSOR" and var1=="PAPER") or (var2=="ROCK" and var1=="SCISSOR"):
        c_count+=1
        var5.set("Computer win")
    else:
        var5.set("Same Sign")

    var3.set(u_count)
    var4.set(c_count)   

put=None
def rock():
    global put
    put="ROCK"
    c_put=random.choice(l)
    var1.set(put)
    var2.set(c_put)
    main_fun1(put,c_put)

def paper():
    global put
    put="PAPER"
    c_put=random.choice(l)
    var1.set(put)
    var2.set(c_put)
    main_fun1(put,c_put)

def sciss():
    global put
    put="SCISSOR"
    c_put=random.choice(l)
    var1.set(put)
    var2.set(c_put)
    main_fun1(put,c_put)    
   
lbl = tkinter.Label(screen,text="** WELCOME TO ROCK PAPER SCISSOR **",font=('arial',25,'bold','underline'),foreground="red",background="khaki")
lbl.place(x=10,y=10)

btn1=tkinter.Button(screen,text="ROCK",font=('arial',30,'bold'),foreground="lime",background="blue",command=rock)
btn1.place(x=50,y=120)

btn2=tkinter.Button(screen,text="PAPER",font=('arial',30,'bold'),foreground="lime",background="blue",command=paper)
btn2.place(x=230,y=120)

btn2=tkinter.Button(screen,text="SCISSOR",font=('arial',30,'bold'),foreground="lime",background="blue",command=sciss)
btn2.place(x=430,y=120)

lbl = tkinter.Label(screen,text="USER",font=('arial',20,'bold'),foreground="blue",background="khaki")
lbl.place(x=80,y=250)

lbl = tkinter.Label(screen,text="COMPUTER",font=('arial',20,'bold'),foreground="blue",background="khaki")
lbl.place(x=50,y=300)

lbl = tkinter.Label(screen,textvariable=var5,font=('arial',30,'bold'),width=15,foreground="cyan",background="olive")
lbl.place(x=165,y=380)

var1_display = tkinter.Label(screen,textvariable=var1,width=8,font=('arial',20,'bold'),foreground="red",background="khaki")
var1_display.place(x=260,y=250)

var2_display = tkinter.Label(screen,textvariable=var2,width=8,font=('arial',20,'bold'),foreground="red",background="khaki")
var2_display.place(x=260,y=300)

var3_display = tkinter.Label(screen,textvariable=var3,width=8,font=('arial',20,'bold'),foreground="red",background="khaki")
var3_display.place(x=500,y=250)

var4_display = tkinter.Label(screen,textvariable=var4,width=8,font=('arial',20,'bold'),foreground="red",background="khaki")
var4_display.place(x=500,y=300)

screen.mainloop()
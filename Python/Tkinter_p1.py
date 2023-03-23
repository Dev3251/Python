import tkinter

screen = tkinter.Tk()
screen.title("Counter")
screen.geometry("500x400")
screen.configure(background="teal")

var1=tkinter.IntVar()
count=0

def addfun():
    global count
    count+=1
    var1.set(count)

def subfun():
    global count
    count-=1
    var1.set(count)

lbl = tkinter.Label(screen,text="WELCOME TO COUNTER",font=('arial',25,'bold'),foreground="yellow",background="teal")
lbl.place(x=40,y=10)

btn1=tkinter.Button(screen,text="+",font=('arial',40,'bold'),foreground="purple",background="yellow",command=addfun)
btn1.place(x=50,y=100)

btn2=tkinter.Button(screen,text="-",font=('arial',40,'bold'),foreground="purple",background="yellow",command=subfun)
btn2.place(x=380,y=100)

var1_display = tkinter.Label(screen,textvariable=var1,font=('arial',70,'bold'),height=1,width=2,foreground="red",background="yellow")
var1_display.place(x=190,y=100)

screen.mainloop()
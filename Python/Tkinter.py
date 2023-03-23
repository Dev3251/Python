import tkinter

screen = tkinter.Tk()
screen.title("Hello")
#width x height
screen.geometry("500x500")
screen.configure(background="yellow")

lbl_var = tkinter.StringVar()

def myfun():
    lbl_var.set("Welcome to My App")
    print("This is my function")
    print("This is my app")

lbl = tkinter.Label(screen,text="WELCOME TO TKINTER",font=('arial',30,'bold'),foreground="blue",background="yellow")
lbl.place(x=10,y=10)

btn = tkinter.Button(screen,text="Click Here",font=('arial',20,'bold'),command=myfun)
btn.place(x=10,y=60)

lbl_display = tkinter.Label(screen,textvariable=lbl_var,font=('arial',30,'bold'),foreground="red",background="yellow")
lbl_display.place(x=10,y=150)

screen.mainloop()
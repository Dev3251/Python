from tkinter import *

screen=Tk()
screen.geometry("500x500")
frame1=Frame(screen,bg="yellow",height="500",width="500")
frame1.grid(row=0,column=0)

l1=[]
for i in range (65,91):
    l1.append(chr(i))

r_count=0
c_count=0
bc_count=0
for txt in l1:
    if r_count<13:
        btn=Button(frame1,text=txt,bg="black",fg="white",font=('arial',20,'bold'))
        btn.grid(row=0,column=c_count)
        r_count+=1
        c_count+=1
    else:
        btn=Button(frame1,text=txt,bg="black",fg="white",font=('arial',20,'bold'))
        btn.grid(row=1,column=bc_count)
        bc_count+=1

def myfun():
    frame1.destroy()
    frame2=Frame(screen,bg="blue",height="500",width="500")
    frame2.grid(row=0,column=0)

    lbl=Label(frame2,text="LABEL",font=('arial',35,'bold'))
    lbl.grid(row=0,column=0)

btn1=Button(frame1,text="NEXT SCREEN",bg="black",fg="white",font=('arial',20,'bold'),command=myfun)
btn1.grid(row=2,column=0,columnspan=13)

screen.mainloop()
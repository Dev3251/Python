from tkinter import *

screen=Tk()
screen.geometry("500x500")

l1=[]
for i in range (1,37):
    l1.append(i)

l2=[1,3,5,7,9,12,14,16,17,19,21,23,25,27,30,32,34,36]

r_count=3
c_count=0
for j in l1:
    if r_count>0:
        if j in l2:
            btn=Button(screen,text=j,bg="red",fg="white",font=('arial',20,'bold'))
            btn.grid(row=r_count,column=c_count)
        else:
            btn=Button(screen,text=j,bg="black",fg="white",font=('arial',20,'bold'))
            btn.grid(row=r_count,column=c_count)
        r_count-=1
        if r_count==0:
            c_count+=1
            r_count=3
            
screen.mainloop()
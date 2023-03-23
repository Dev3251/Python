from tkinter import * 
import pymysql
from my_db_connection import *

myconnection() 
screen = Tk() 
screen.geometry("500x500")

e1_var = StringVar() 
e2_var = StringVar() 
e3_var = StringVar() 
lbl_message = StringVar()
#----------------------- logic ------------------------

mydb = pymysql.connect(host="localhost",user="root",password="",database="Python")
mycursor = mydb.cursor() 

def addData():
    query = "insert into student (firstname,lastname,subject)  values ('%s','%s','%s') "
    values = (e1_var.get(),e2_var.get(),e3_var.get())

    mycursor.execute(query%values)
    mydb.commit() 
    lbl_message.set("successfully data inserted !!!")

def updatedata():
    query = "update student set lastname = '%s' ,subject='%s' where firstname='%s'"
    values = (e2_var.get(),e3_var.get(),e1_var.get())

    mycursor.execute(query%values)
    mydb.commit() 
    lbl_message.set("successfully data updated !!!")

def deletedata():
    query = "delete from student where firstname='%s'"
    values = (e1_var.get())

    mycursor.execute(query%values)
    mydb.commit() 
    lbl_message.set("successfully data deleted !!!")

def searchData():
    query = "select * from student where firstname = '%s' "
    values = (e1_var.get())

    mycursor.execute(query%values)
    data = mycursor.fetchone()

    e2_var.set(data[2])
    e3_var.set(data[3])

#----------------------- logic ------------------------


#-------------------------- designing ---------------------------------
lbl = Label(screen,text="Enter your firstname : ",font=('arial',12,'bold'))
lbl.place(x=10,y=10)

e1 = Entry(screen,textvariable=e1_var)
e1.place(x=200,y=10)


lbl = Label(screen,text="Enter your lastname : ",font=('arial',12,'bold'))
lbl.place(x=10,y=60)

e1 = Entry(screen,textvariable=e2_var)
e1.place(x=200,y=60)

lbl = Label(screen,text="Enter your subject : ",font=('arial',12,'bold'))
lbl.place(x=10,y=120)

e1 = Entry(screen,textvariable=e3_var)
e1.place(x=200,y=120)


btn = Button(screen,text="SAVE",width=5,command=addData)
btn.place(x=20,y=160)

lbl = Label(screen,textvariable=lbl_message)
lbl.place(x=100,y=250)

btn_update=Button(screen,text="UPDATE",width=5,command=updatedata)
btn_update.place(x=100,y=160)

btn_delete=Button(screen,text="DELETE",width=5,command=deletedata)
btn_delete.place(x=160,y=160)

btn_search = Button(screen,text="Search",width=5,command=searchData)
btn_search.place(x=220,y=160)

#-------------------------- designing ---------------------------------

screen.mainloop() 
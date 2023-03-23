# pip install pymysql 
import pymysql

def myconnection():
    # connection with mysql 
    mydb = pymysql.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor() 

    mycursor.execute("create database if not exists Python")
    mydb.commit() # save 

    # connection with database 
    mydb = pymysql.connect(host="localhost",user="root",password="",database="Python")
    mycursor = mydb.cursor() 

    mycursor.execute("create table if not exists  student (id int primary key auto_increment not null , firstname varchar(20), lastname varchar(20), subject varchar(20) )  ")
    mydb.commit() 
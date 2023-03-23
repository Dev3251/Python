"""

OOPS : object oriented programing system

class
object
inheritance
encapsulation
abstraction
polymorphism


class : class is a user defined datatype which is contain data member and member functions.

syntax :

class <classname>:
    statement

obj=class
obj.property()    

"""
#self : self is inbuilt keyword which is used to repersent current class property

class Student:
    def display(self):
        print("Hello")

obj = Student()
obj.display()        
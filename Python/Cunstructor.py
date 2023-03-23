# cunstructor : It is invoked when object of class is created 
class Student:
    def __init__(self,fname,subject):
        self.fname=fname
        self.subject=subject

    def display(self):
        print(self.fname)
        print(self.subject)

j = Student("Hritik","Python")
j.display()

s = Student("Alia","Java")
s.display()
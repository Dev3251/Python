"""

Encapsulation : Encapsulation which contain data member and member function in single entity

whcih contains getter and setter

def setId():
    //code of set data

def getId():
    //retrive data from class

"""
class Student:
    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

obj = Student()
obj.setId(101) 
obj.setName("Dev")

print(obj.getId())
print(obj.getName())
"""

inheritace : one class derived proprties of another class its called inheritance

By using it we can reduce and reuse code

Types of Inheritance :

1) Single level
2) Multi level
3) Multiple
4) Hierchical
5) Hybrid

"""

# single level 

class A:
    def displayA(self):
        print("A class here")

class B(A):
    def displayB(self):
        print("B class here")  

obj = B()
obj.displayA()
obj.displayB()
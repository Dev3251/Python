class A:
    def displayA(self):
        print("Class A")

class B(A):
    def displayB(self):
        print("Class B") 

class C(A):        
    def displayC(self):
        print("Class C")

class D(B):
    def displayD(self):
        print("Class D")

obj1 = D()
obj1.displayA()
obj1.displayB()
obj1.displayD()

obj2 = C()
obj2.displayA()
obj2.displayC()

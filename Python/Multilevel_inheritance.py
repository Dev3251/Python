class A:
    def inputA(self,num1):
        self.num1=num1

    def displayA(self):
        print(self.num1)

class B(A):
    def inputB(self,num2):
         self.num2=num2

    def diaplayB(self):
        print(self.num2)

class C(B):
    def addition(self):
        print(self.num1 + self.num2)

obj = C()
obj.inputA(10)
obj.displayA()
obj.inputB(20)
obj.diaplayB()
obj.addition()
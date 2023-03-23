class A:
    def inputA(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def displayA(self):
        print(self.num1)
        print(self.num2)

class B(A):
    def inputB(self):
        self.ans = self.num1 + self.num2

    def diaplayB(self):
        print(self.ans)

obj = B()
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

obj.inputA(num1,num2)
obj.displayA()
obj.inputB()
obj.diaplayB()
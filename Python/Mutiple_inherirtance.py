class A:
    def inputA(self,num1):
        self.num1=num1

class B:
    def inputB(self,num2):
        self.num2=num2        

class C(A,B):
    def display(self):
        self.ans=self.num1+self.num2
        print("Ans : ",self.ans)

obj = C()
obj.inputA(10)
obj.inputB(20)
obj.display()
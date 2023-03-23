"""

Access modidiers :

__element : private (which is access by own class only)

_element : protected (which is access by own class and his child class)

element : public (which can access by any class)
"""

class A:
    def __init__(self):
        self.mobile = 10000
        self.__computer = 20000

    def display(self):
        print(self.mobile) 
        print(self.__computer)

obj = A()
obj.display()

obj.mobile=50000
obj.__computer=70000

obj.display()
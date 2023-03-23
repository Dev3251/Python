"""
Abstraction : which is provide only few information not allocated background information

"""
# ABC = Abstract Base Class
from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def roi(self):
        print("5.5")

class HDFC(RBI):
    def roi(self):
        print("7.5")

sbi_obj=SBI()
hdfc_obj=HDFC()

sbi_obj.roi()
hdfc_obj.roi()
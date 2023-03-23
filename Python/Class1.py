class Pro:
    def oddeven(self,num):
        if num%2==0:
            return "Even"
        else:
            return "Odd"

obj = Pro()
print(obj.oddeven(10))
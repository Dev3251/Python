"""
Exception handaling ::

Exception : Which disturb the normal flow of the program 

To handle this kind of exception  
need to use try and except block

"""
# print(a)
a=10
try:
    num1=int(input("Enter number :"))
    ans=num1*num1
    print(ans)
except:
    print("Invalid Input")

print(a)    
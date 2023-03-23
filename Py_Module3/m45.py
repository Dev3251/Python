def factorial(x):
    s=1
    while(x!=1):
        s=s*x
        x-=1
    return s

a=int(input("Enter the number : "))
if(a<0):
    print("Please enter possitive numbers !!")
else:
    print(factorial(a))
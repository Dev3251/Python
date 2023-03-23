try:
    n1=int(input("Enter Number 1 :"))
    n2=int(input("Enter Number 2 :"))

    ans=n1/n2

    print(ans)
except ValueError:
    print("Only Numbers Required")
except ZeroDivisionError:
    print("Can not divisible by zero")        
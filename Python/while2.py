status=True
while status:
    num=int(input("Enter number : "))
    if num%2==0:
        print("Even")
    else:
        print("Odd")

    choice=input("Do you want to continue ? press y for yes and n for no : ")
    if choice=='n' or choice=='no':
        status=False        
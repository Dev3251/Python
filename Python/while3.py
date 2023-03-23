from operator import truediv
import random

status = True

while status:
    num=random.randint(1,100)
    print(num)
    choice=input("Do you want to continue ? press y for yes and n for no : ")
    if choice=='y' or choice=='yes':
        status=True
    elif choice=='n' or choice=='no':
        status=False   
    else:
        print("INVALID INPUT !!")
        status=False     
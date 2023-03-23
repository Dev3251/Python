import random

status=True
computer=random.randint(1,100)

while status:
    user=int(input("Enter number : "))
    if user>computer:
        print("HINT : GUESS LOWER NUMBER")
    elif user<computer:
         print("HINT : GUESS HIGHER NUMBER")
    else:
        print("YOU WINNNN !!")
        status=False

       
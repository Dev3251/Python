print("----------------------------------")
print("Welcome To Kalyan Jwelers")
print("----------------------------------")
name=input("Enter Your Name : ")
gen=input("Enter Your Gender : ")
age=int(input("Enter Your Age : "))
py=0
status=True
while status!=False:
    item=input("Enter Name of Gold Product : ")
    weight=int(input("Enter The Weight of Product (Grams): "))
    tp=int(input("Today's Price Of 1 Gram(22K) Gold : "))
    mp=int(input("Enter Making Charges : "))
    fp=(tp+mp)*weight
    print("----------------------------------")
    print("Kalyan Jwelers  Conatct:9857546562")
    print("----------------------------------")
    print("| Name : ",name )
    print("| Gender : ",gen)
    print("| Age : ",age)
    print("| Gold Product : ",item)
    print("| Gold Product Weight : ",weight)
    print("| Today's Gold Price : ",tp)
    print("| Total Gold Price : ",tp*weight)
    print("| Total Making Charges : ",mp*weight)
    print("| Total Amount : ",fp)
    print("----------------------------------")
    if gen=='Female':
        if age>30:
            if weight>=1 and weight<=20:
                fp*=0.95
                print("| Discount : 5%")
            elif weight>=20 and weight<=40:
                fp*=0.9
                print("| Discount : 10%")
            else:         
                fp*=0.8
                print("| Discount : 20%")
        else:
            if weight>=1 and weight<=20:
                fp*=0.9
                print("| Discount : 10%")
            elif weight>=20 and weight<=40:
                fp*=0.8
                print("| Discount : 20%")
            else:         
                fp*=0.7
                print("| Discount : 30%")
    else:
        if age>30:
            if weight>=1 and weight<=20:
                fp*=0.9
                print("| Discount : 10%")
            elif weight>=20 and weight<=40:
                fp*=0.8
                print("| Discount : 20%")
            else:         
                fp*=0.7
                print("| Discount : 30%")
        else:
            if weight>=1 and weight<=20:
                fp*=0.8
                print("| Discount : 20%")
            elif weight>=20 and weight<=40:
                fp*=0.7
                print("| Discount : 30%")
            else:         
                fp*=0.6
                print("| Discount : 40%")
    print("| Net Amount : ",fp)           
    print("----------------------------------")
    py+=fp
    choice=input("Do You Want To Add More Products Press y for yes and no for no :")
    if choice=='y' or choice=='yes':
        status=True
    elif choice=='n' or choice=='no':
        status=False   
    else:
        print("INVALID INPUT !!")
        status=False
print("----------------------------------")
print("Payment : ",py)   
print("----------------------------------")
print("Thank You Visit Again !!")
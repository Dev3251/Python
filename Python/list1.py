from secrets import choice


l1=[]

menu="""
                    MENU

        1) PRESSS 1 FOR ADD PRODUCT 
        2) PRESSS 2 FOR REMOVE PRODUCT
        3) PRESSS 3 FOR VIEW PRODUCT    

        """
status=True
while status:
    print(menu)
    choice=int(input("Enter choice : "))
    if choice==1:
        p_name=input("Enter product name : ")
        l1.append(p_name)
    elif choice==2:
        r_name=input("Enter product name : ")
        l1.remove(r_name)
    elif choice==3:
        for p in l1:
            print(p)
   
    ch=input("Do you want to perform new operations : press 'y' for yes and 'n' for no : ") 
    if ch=='n' or ch=='no':
        status=False
    else:
        status=True       
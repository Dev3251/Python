menu1="""
                ********************************************
                    ITEM                            PRICE
                ********************************************

                   VADAPAV                           30
                   DABELI                            25
                   SANDWHICH                         50
                   BURGER                            70
                   PUFF                              35  
                *********************************************
    """
menu="""
                    MENU

        1) PRESSS 1 FOR ADD PRODUCT 
        2) PRESSS 2 FOR REMOVE PRODUCT
        3) PRESSS 3 FOR VIEW PRODUCT    

        """    
l1=["Vadapav","Dabeli","Sandwhich","Burger","Puff"]
l2=[30,25,50,70,35]

for i in l1:
    index=l1.index(i)
    print(f"{i} = {l2[index]}")
fp=0
status=True
while status:
    print(menu)
    choice=int(input("Enter choice : "))
    if choice==1:
        p_name=input("Enter product name : ")
    elif choice==2:
        r_name=input("Enter product name : ")
        l1.remove(r_name)
    elif choice==3:
        for p in l1:
            print(p)
   
    print(fp)
    ch=input("Do you want to perform new operations : press 'y' for yes and 'n' for no : ") 
    if ch=='n' or ch=='no':
        status=False
    else:
        status=True           
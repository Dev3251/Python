menu="""
                    MENU

            press 1 for product manager
            press 2 for customer        
"""
status=True
main_stock={}

m_status=True
while m_status:
    print(menu)
    u_choice=int(input("Enter your choice : "))
    if u_choice==1:
        print("------------Main Stock--------------")
        print(main_stock)
        while status:
            main_specification={}
            print("PRODUCT MANAGER")
            p_brand=input("Enter product brand : ")
            p_name=input("Enter product name : ")
            qty=int(input("Enter no. of qty :"))
            price=int(input("Enter price :"))   

            main_specification['p_name']=p_name
            main_specification['qty']=qty
            main_specification['price']=price

            main_stock[p_brand]=main_specification
            print(main_stock)
            
            choice=input("Do You Want To Add More Products Press y for yes and no for no :").lower()
            if choice=='y' or choice=='yes':
                status=True
            elif choice=='n' or choice=='no':
                status=False   
            else:
                print("INVALID INPUT !!")
                status=False

    else:
        print("CUSTOMER")    

        for k in main_stock.keys():
            print(f"---------- {k} ----------")
            print("Procduct Name : ",main_stock[k]["p_name"])
            print("Price :",main_stock[k]["price"])

        p_brand=input("Enter product brand : ")
        p_name=input("Enter product name : ")
        qty=int(input("Enter no. of qty do you want ?"))    
        price=main_stock[p_brand]["price"]
        print("ACTUAL PRICE : ",price)
        tp=qty*price
        print("TOTAL PRICE :",tp)
        proceed_menu=input("Do you want to proceed this product :")
        new_qty=main_stock[p_brand]['qty']-qty

        if proceed_menu=='y':
            main_stock[p_brand]['qty']=new_qty
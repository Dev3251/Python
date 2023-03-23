menu="""
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
print(menu)
main_product={}

status=True

while status:
    product_name=input("Enter product : ").upper()
    if product_name == 'VADAPAV':
        price=30
    elif product_name == 'DABELI':
        price=25
    elif product_name == 'SANDWHICH':
        price=50
    elif product_name == 'BURGER':
        price=70
    elif product_name == 'PUFF':
        price=35    

    main_product[product_name]=price
    choice=input("Do You Want To Add More Products Press y for yes and no for no :").lower()
    if choice=='y' or choice=='yes':
        status=True
    elif choice=='n' or choice=='no':
        status=False   
    else:
        print("INVALID INPUT !!")
        status=False

print(main_product)
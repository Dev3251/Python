f=open("file.txt","a")

status=True

while status:
    content=input()
    f.write("\n"+content)

    choice=input("Do You Want To Add More content y for yes and no for no :")
    if choice=='y' or choice=='yes':
        status=True
    elif choice=='n' or choice=='no':
        status=False   

f.close()        
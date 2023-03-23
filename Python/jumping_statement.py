"""
jumping statements :

1) break : it will break the loop 
2) continue : it will skip the current statement 
3) pass : nothing to display

"""
# for i in range(1,6):
#     num=int(input("Enter a number : "))
#     if num>35:
#         print("Pass")
#     else:
#         print("Fail")  
#         break  

for i in range(1,6):
    num=int(input("Enter a number : "))
    if num>35:
        print("Pass")
    else: 
        continue
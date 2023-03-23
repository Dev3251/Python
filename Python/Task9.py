count1=0
count2=0
for i in range(1,6):
    num = int(input(f"Enter numner {i} : "))
    if num%2==0:
        count1=count1+1
    else:
        count2=count2+1

print("Total Odd numbers :",count2)            
print("Total Even numbers :",count1)
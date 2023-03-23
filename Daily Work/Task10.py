sum1=0
sum2=0
for i in range(1,6):
    num = int(input(f"Enter numner {i} : "))
    if num%2==0:
        sum1=sum1+num
    else:
        sum2=sum2+num

print("Sum of Odd numbers :",sum2)            
print("Sum of Even numbers :",sum1)
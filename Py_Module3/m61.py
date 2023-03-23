a=int(input("Enter the number : "))
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i

print(f"The sum of all divisiors of {a} : ",sum)
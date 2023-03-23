for i in range(1,6):
    if i%2==0:
        print(f"{i} even number")
    else:
        print(f"{i} odd number")

sum = 0 
for j in range(1,6):
    num = int(input(f"Enter number {j} : "))
    sum=sum+num

print("Sum =",sum)           
    
l1=[]
l2=[]
for i in range(1,6):
    num=int(input("Enter number : "))
    if num%2==0:
        l1.append(num)
    else:
        l2.append(num)   
print("Even List :---")
for i in l1:
    print(i)
print("Odd List :---")
for j in l2:
    print(j)

print("Even List :---")
for i in l1:
    print(i,end=" ")

print()
print("Odd List :---")
for j in l2:
    print(j,end=" ")
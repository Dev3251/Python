a=int(input("Enter the number : "))
n1,n2=0,1
count=0

print("Fibonaci series : ")
while count<a:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1
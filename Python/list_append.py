"""

add element in existing list 

1) append() : we can add single element in existing list 
2) insert() : we can add specific element at specific location (index) 
3) extend() : we can add multiple elements in existing list 
"""
l1=[2]
for i in range(1,6):
    num=int(input("Enter number : "))
    l1.append(num)

print(l1)

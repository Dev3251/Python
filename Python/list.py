"""

Collection : collection means which is contain number of elements in single location 

There are 4 types of collection :

1) List
2) Tuple
3) Set
4) Dictionary

1) List : list is a collection of data type which is contain similar and dis-similar 
          data elements in single location.

list which is represent by []

list which is mutuable(we can change it value)

list are indexable,orderable
"""

#blank list :

l1=[]
print(l1)

l2=[99,12,23,34,45,56,67,78,89]
print(l2)

for i in l2:
    print(i)

print("First element : ",l2[0])
print("Last element : ",l2[-1])
print("Range : ",l2[3:6])

print(max(l2))
print(min(l2))
print(sum(l2))

l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)

l2.reverse()
print(l2)
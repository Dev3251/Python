"""
tuple : tuple is a collection data which is contain similar and dis-similar data elements.

tuple is represent by ()

tuples are immutable - we can't change it's value
"""

from tkinter import Canvas


t=()
print(t)

t=("C","C++","Java")
print(t)

print(len(t))

# If we can put only one item in tuple then it will be considered as string otherwise tuple.
t=("Python")
print(type(t))
print(t)

# we can't change the value 

t=("Python","C++")
l1=list(t)
l1[1]="Java"
t=tuple(l1)
print(t)

t=("C","C++","Java","Python")
print(t)

for i in t:
    print(i)

t=("C","C++","Java","Python","C","Java")
print(t.count("Java"))
print(t)
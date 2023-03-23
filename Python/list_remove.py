"""
remove: to remove an element from the list

pop(): it will remove last element from the list

pop(index): remove element with specific position

clear : to remove all elemnts from list

del :to remove all elements with variable or object
"""
l1=[12,23,34,45,56,78,89]
print(l1)

l1.remove(34)
print(l1)

l1.pop()
print(l1)

l1.pop(1)
print(l1)

l1.clear()
print(l1)

del l1
print(l1)
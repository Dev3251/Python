"""
dictionary is a most powerful concept in collection which contains key and values pair

dictionary is represent by {}
"""

Student = {
    "Id" : 1,
    "Name" : "Dev",
    "Subject" : "Python",
    "Marks" : 90,
}
print(Student)
print(Student.keys())
print(Student.values())

for k,v in Student.items():
    print(f'{k} = {v}')
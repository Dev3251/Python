"""
nested if statement 

syntax :

if condition :
    statement
    if condition :
        statement
    else:
        statement
else:
    if condition :
        statement
    else:
        statement

"""
ind = int(input("Ennter India score :"))
aus = int(input("Ennter Austrelia score :"))
pak = int(input("Ennter Pakistan score :"))

if aus>pak:
    if aus>ind:
        print("Austrelia won the match")
    else:
        print("India won the match")   
else:
    if pak>ind:
        print("Pakistan won the match")
    else:
        print("India won the match")
    
        

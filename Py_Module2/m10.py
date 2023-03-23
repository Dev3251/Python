def test_num(a,b):
    if a==b or a+b==5 or a-b==5 or b-a==5:
        return True
    else:
        return False

print(test_num(5,5))
print(test_num(3,2))
print(test_num(15,10))
print(test_num(7,4))
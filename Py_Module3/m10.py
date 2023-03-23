def compare_list(l1,l2):
    status=False
    for x in l1:
        for y in l2:
            if x==y:
                status=True
                return status

l1=[1,2,3,4,5]
l2=[2,3,4,5,6]
print(compare_list(l1,l2))
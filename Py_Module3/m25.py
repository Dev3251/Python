def list_duplicate(l):
    f_list=[]
    for num in l:
        if num not in f_list:
         f_list.append(num)
    return f_list

t1=(1,2,3,5,4,8,3,9,8,7,2,1)
l1=list(t1)
l1=list_duplicate(l1)
t=tuple(l1)
print(t)
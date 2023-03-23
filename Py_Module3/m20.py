def check_tuple(t):
    if len(t)==0:
        print("Tuple is empty")
    else:
        print("Tuple is not empty")

l1=(1,2,3)
l2=()
check_tuple(l1)
check_tuple(l2)
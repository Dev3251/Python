def check_key(dic,key):
    if key in dic.keys():
        print("Key is present in dictionary")
    else:
        print("Key is not present in dictionary")

dic={'a':1,'b':2,'c':3}
check_key(dic,'a')
check_key(dic,'w')
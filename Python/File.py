"""

File Handaling : To create ,read and open file

In python there are 3 modes which is used to acsess and edit 

1) read - r
2) write - w
3) append - a
4) create blank file - x 

"""

f=open("file.txt")
print(f.read())
f.close()

f=open("file.txt","w")
f.write("Computer Engineering")
f.write("Python Developer")
f.close()
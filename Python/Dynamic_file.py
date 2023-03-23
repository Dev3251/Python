"""

when we use w mode it always work with single file
w mode write once and overwrite previous content

"""
f=open("file.txt","w")
name = input("Enter Content : ")
f.write(name)

f.close()
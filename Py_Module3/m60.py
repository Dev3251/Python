pi=22/7
h=float(input("Enter the height of cylinder : "))
r=float(input("Enter the radius of cylinder : "))
volume = pi*(r**2)*h
surface_area = 2*pi*r*(r+h)
print("Volume : ",volume)
print("Surface Area : ",surface_area)
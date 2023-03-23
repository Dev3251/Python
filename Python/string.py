email = "dkduhdia@gmail.com"
password = "3251"

u_email = input("Enter email : ")
u_password = input("Enter password : ")

if u_email==email and u_password==password:
    print("Login successfully !!")
else:
    if u_email!=email and u_password!=password:
        print("Email and Password are incorrect")
    elif  u_email!=email:
        print("Invalid Email")
    elif  u_password!=password:
        print("Invalid Password")     

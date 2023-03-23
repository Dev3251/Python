score=0
def qu1():
    global score
    print("Q.1  Who is developed C language ?")
    print("A. Danis Ritchie")
    print("B. Andy Rubin")
    ans=input("Enter your ans. : ")
    if ans=='A':
        score+=50
        print("Right Answer")
    else:
        score-=20
        print("Wrong Answer")

def qu2():
    global score
    print("Q.2  Which is most popular language ?")
    print("A. Java")
    print("B. Python")
    ans=input("Enter your ans. : ")
    if ans=='B':
        score+=50
        print("Right Answer")
    else:
        score-=20
        print("Wrong Answer")            

qu1()
qu2()
print("Score = ",score)        
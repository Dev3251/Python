Quiz={
    1:{
        "que" : "Que. Who is Prime Minister of India ?",
        "ans" : "Narendra Modi",
    },
    2:{
        "que" : "Que. What is the most popular programming language ?",
        "ans" : "Python",
    },
}

size=len(Quiz)

for i in range(1,size+1):
    print(Quiz[i]["que"])
    ans=input("Ans. ")
    if ans==Quiz[i]["ans"]:
        print("Correct Answer.")
    else:
        print("Incorrect Answer.")    


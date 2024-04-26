import random

def computerchoice():
    
    col = ["RED","ORANGE","YELLOW","GREEN","BLUE","PINK","WHITE","BLACK"]
    a = random.choice(col)
    return a

Answers= []
#computerchoice =[] 
for i in range(4):
    Answers.append(computerchoice())
    print(Answers)
   
   
   #i<4 Answers.ammend(computerchoice[])
 

    

A  = input("Enter 4 colours with spaces between them")
Ucolour = A.split()
print(Ucolour)

"if  A == "
"""
for i in range(4):
    x=0
for u in range(4):
    f=0
    y=0
if Ucolour[x] == Answers[y]:
    y = y +1
    f = f +1
    print("correct coloour correct place")

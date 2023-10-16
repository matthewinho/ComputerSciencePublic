import random
"""
num1 = random.randint(1,100)

print(num1)

list1 = ("apple" , "banana" , "orange" , "mango" , "grape" )
a = random.choice(list1 )
print(a)"""

"""

loo =("HEADS" , "TAILS")

ht = random.choice(loo)
hta = input("HEADS OR TAILS ")
if hta == ht:
    print(ht)
    print("yo win")
    """

#55

"""ra = random.randint(1,5)
ca = int(input("Pick a number!  "))
if ca == ra:
    print("Well done")
while ca<ra or ca>ra:
    print("WRONG")
    cb= int(input("Choose another number"))
    if cb == ra:
        print("Well done")
        break """
    
   #56 
    
"""ra = random.randint(1,10)
ca = int(input("Pick a number!  "))
if ca == ra:
    print("Well done")
if ca<ra:
    print("NUH UH TOO LOW")
if ca>ra:
    print("NUH UH TOO HIGH")
while ca<ra or ca>ra:
    print("too low")
    cb= int(input("Choose another number"))
    if cb == ra:
        print("Well done")
        break    """    
    
    
#57





#58


#a = ("whats your age plus 6", "whats




#while True:
print("-- QUIZ -- 5 RANDOM QUESTIONS --")
num1 = random.randint(1,100)
num2 = random.randint(1,100)

#while True:
#num1 = random.randint(1,5)
#num2 = random.randint(1,5)
num4 = random.randint(2,6)
score = 0
ak = num1+ num2
ak1 = ak * 3
#score = score + 1
#score1 = score +1

"""print(num1, num2)
answer = int(input("Whats the first number added with the second number  : "))
if answer == ak:
    score = score + 1
    print(" Congrats ur score is:" , score, ": NEXT QUESTION  ")
else:
     print(" wrong.. next question ")
     
print(ak)     
a=  int(input("whats this multiplied by 3 "))
if a == ak1:
    score = score + 1
    print(" Congrats ur score is:" , score, ": NEXT QUESTION  ")
else:
    print(" wrong.. next question ", score -1)  
       
print("whats" ,num4, "divided by 2 to the NEAREST whole number")
a= int(input(" ur answer is : "))
if a == num4 //2 :
    score = score + 1
    print(" --Congrats ur score is:" , score, "NEXT QUESTION  YOUR NEARLY THERE 2 MORE QUESTIONS TO GO-- ")
else:
     print(" wrong.. next question your SCORE IS", score -1)
     
print(num1, num2)
blob = int(input("Whats the first number minus  the second number  : "))
if blob - ak:
    score = score + 1
    print(" Congrats ur score is:" , score, ": NEXT QUESTION  ")
else:
     print(" wrong.. next question ")
print("FINAL AND LAST QUESTION")
"""
"""
print(num1)
ba = int(input("whats this squaraed multiplied by 5"))
if ba == num1*num1*5:
    print("CONGRATS QUIZ OVER YAYAYAY")
else:
    print("your dookie")
"""

#59
    

yoyo = True

lol = random.choice(["red","orange","yellow","green","blue"])
colours = ["red","orange","yellow","green","blue"]
print(colours)
while yoyo == True:
    C = input("GUESS WHICH COLOUR I CHOSE ")
    if C == lol:
        print("YOU GOT ME")
        break
    if C == "red":
        print("WRONG i left yo mom on red lil buddy")
    if C == "orange":
        print("WRONG bet your orange like Trump lil buddy")
    if C == "yellow":
        print("WRONG yellow minion headass")
    if C == "green":
        print("WRONG you green and sick lil guy?")
    if C == "blue":
        print("WRONG blue smurf headass?")
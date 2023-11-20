#120
import random

print("1) ADDITION")
print("2) SUBTRACTION")
a = int(input(" Enter 1 or 2 "))
if a ==1:
    b = random.randint(5,20)
    c = random.randint(5,20)
    add  = c,b
    sl = c+b
    print(add)
boy = int(input(" what are these two numbers added together"))
if boy == sl:
    print("Thats the correct answer. congratz")
else:
    print("your answer" ,b ,"is incorrect ,the actual answer is" , sl)
    
if a == 2:
     d = random.randint(25,50)
     e = random.randint(1,25)
     lol = a-d
     bagel = int(input("whats" , d , "minus" , e))
if bagel == lol:
    print("correct")
else:
    print("wrong, the correct answer is", lol)
     
    
        
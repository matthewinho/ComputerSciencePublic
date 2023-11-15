

"""

def sub(x):
    
    print(x)

sub(432)
"""

# if u put something in for "x" , it will be that value


"""
def sub():
    num = int(input("Enter a  number"))
 
    b = 0
    while b<num:
            b  = b + 1 
            print(b)
 
result = sub()
"""


import random

#part(i)
def poo():
    
    h = int(input("enter a high number  "))
    l = int(input("Enter a low number  "))
    return  random.randint(l,h)
    
    
    return poo()

compnum  = poo()
print(compnum)


#119 (ii)

def silly():
     a = int(input("Im thinking of a number between 1-10 ... try guess it "))
     b  = random.randint(1,10)
     if a == b:
         print("You have guessed the RIGHT number.!!")
     else:
         print("wrong")
         return silly()
     return ''
gaga = silly()
#a = print()
#print(a)
print(gaga)


#119 (iii)

"""
def pog()
ba = int(input(" check if  " ,compnum ," is the same as the gussed number")) 
if compnum == b
print("Congratz u win")
if compnum > b
"""




#120
#print("1) ADDITION")
#print("2) SUBTRACTION")
#print("3) Enter 1 or 2 ")

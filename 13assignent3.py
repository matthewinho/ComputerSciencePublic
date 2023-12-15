
#1
 
"""
 
for i in range (1,11):
 
    print(i)
 
 
#2
 
 
for a in range(20,0,-1):
 
    print(a)
 
 


 



#6
 
for h  in  [1,2,3,4,5]:
 
   print("happy birthday")

"""  

"""

#3

 
for num in range(1, 11):

    if num % 2 == 0:

        print(num)


#4


n = 20
 
 
for i in range(1,n):

     print(i)

"""    

#5

"""

n = 20

for z in range(1,n,2):

    print(z)

"""
 
#7

"""

n = int(input("Enter a number: "))
 
print("The first", n, "terms of the series are:", end=" ")

for i in range(1, n+1):

    print(i**2, end=" ")

"""       

#8

"""  

a = int(input("Enter a number: "))
 
print("Multiplication table for", a)

for i in range(1, 13):

    print(a, "x", i, "=", a * i)
"""
"""
#9

for g in range(3,32,4):

    print(g)
"""

"""
#10

v = 2

ratio= 3
 
 
for i in range(6):

    XD =   v * (ratio ** i)

    print(XD)
    
"""
# DO THIS IF U WANT TO FIND THE SUM OF A BUNCH OF NUMBERS
#11
"""
b  = 0
c = 0 

n =  int(input("enter a number"))

for i in range (0,n):
    
    b = b+1
    c = c+b
    print(b)
    
    
print(c)



"""

#12
"""
n = int(input("enter a POSITIVE number"))

b  = 0
c = 0 
frac = 0
# frac and b known as 
for i in range (0,n):
    b = b+1
    c = c+b
    print(b)
    frac =  frac + 1/b
    
    
#print(c)
         
#frac =  1/b
a = round(frac,2)
print(a)
"""
"""

#13 # you are probably meant to use in range 
a = int(input("input enter a number"))
b = int(input("input enter a SECOND  number"))
c = int(input("input enter a  THIRD number"))
d = int(input("input enter a FOURTH number"))
e = int(input("input enter a  FIFTH number"))
lol = a+b+c+d+e

print(lol)
"""



#for i in range(5) shold have looped it 




#14

"""b  = 0
multiply = 1 

n =  int(input("enter a number"))
if n <= 0 :
    print("incorrect cant enter a negative number")
for i in range (0,n):
    
    b = b+1
    multiply = multiply*b
    print(multiply)"""

    
#15
    

base = int(input("Enter a base number"))
exp = int(input("Enter an exponent number"))
c = 0
for i in range (exp-1):   
    c = base * base 
print (c)

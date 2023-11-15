#PART 3



 
a = int(input("enter your first random number  "))
b = int(input("enter your second random number  "))
c = int(input("enter your third random number  "))
 
if a > b and a > c:
    print(" a is the greatest number")
#if a > c:
#    print(" a is the greatest number")
else b>a and b>c:
    print("b is the greatest number")
if c>b or c>a:
    print(" c is the greatest number")
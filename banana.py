"""
#1
a= int(input("insert a number "))
b= int(input("insert a 2nd number "))

c = a+b


def add(a,b):
    c = a+b
    
    return(c)
"""
"""
#2
po = input("Enter a word")

def add(po):
    b = "un"
    caca =b+po
    
    return(caca)
"""
#print(add(po))
#3
""

p = input("enter any word or a palindrome  ")

ans =  ("your word is a palindrome")

wro = (" not a palindrome")

def palin(p):
    
    reverse = p[::-1]

    if reverse == p:
        return(ans )
    if reverse != p:
        return(wro )
print(palin(p))


"""
#4
list1 = [1,2,3,4,5,6,7,8,9,10]

b = list1 % 2

list1.remove(b)
print(list1)

"""


"""
lol = int(input("Deciaml"))

def binary(A):

    Binary = []

    while A > 0:

        B = A//16

        remainder = A % 16

        if remainder == 10:

            remainder = "A"

        if remainder == 11:

            remainder = "B"

        if remainder == 12:

            remainder = "C"

        if remainder == 13:

            remainder = "D"

        if remainder == 14:

            remainder = "E"

        if remainder == 15:

            remainder = "F"
 
 
        Binary.insert(0,remainder)

        A = B

    return (Binary)

X = binary(lol)
 
 


print(X)
"""
def binary(U):

     ba = []

     while U>0:

 


         a = U%2

         U = U//2

         no = U
 
         #(U, "remainder", a)

         ba.append(a)
 
 


     ba.reverse()

 
     return ba

 
def decimal(no):



      #  print(word[0])

        U = (ord(letter))

        a = binary(U)


        return  a

no = (input("enter a the a letter"))
list1 = []
for letter in no:

    ans = decimal(no)

    print(ans,end =" ")
   
    list1.append(ans)

L = len(ans)
print(L)
"""
if L <= 7:
    list1.insert(0,0)
    
else:
    print("bruh")
"""
"""

test1 = []
test2 = []
if L <= 11:
     
     test1.append(110)
     
    
     a = list1[1:5]
     test1.append(a)
     b = list1[5:11]
     test2.append(10)
     
     
     #test1.append(a)
     print("ans",test1)
     print("check",test2,b)
"""
   
    
#int("10101010101",2)
#1365
#chr(1365)
#Օ
"""
print(L)
for o in range(len(list1)):
    L = len(list1[o])
    
    BA = 8 - L
    for i in range(BA):
        list1[o].insert(0,0)
         
#add = sum(list1)
print("\nUTF-8 code format",list1)
print(L)
"""
#if L <= 11:

"""
add =[]


add[0] = list1
print(len(add))
    
"""

g = []
f = []
h =[]
if L <= 14:
    g.append(1110)
    MJ = ans[0:4]
    ban = g + MJ
  #  g.append(MJ)
    print(ban)
    f.append(10)
    JM = ans[4:10]
    
    can = f +JM
    
    print(can)
    h.append(10)
    KM = ans[10:14]
    baka = g + KM
    print(baka)

    
gg = []
ll = []
kk=[]
hh = []
if L <= 21:
    gg.append(11110)
    pop = ans[0:3]
    zan = gg + pop
    print(zan)
    
    ll.append(10)
    JK = ans[4:10]
    candy = ll +JK
    print(candy)
    
    kk.append(10)
    UP = ans[10:16]
    kaka = kk + UP
    print(kaka)
    
    hh.append(10)
    klop = ans[16:-1]
    zana = hh + klop
    print(zana)
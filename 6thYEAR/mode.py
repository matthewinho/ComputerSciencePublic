#MODE
L = [int(item) for item in input("Enter a list with spaces in between :").split()]
a = -1


n = len(L)
for i in range (0,n):
     a = a +1
     b = L[a]
     test = L.count(b)
     
   
print(test, " =  THE MODE")
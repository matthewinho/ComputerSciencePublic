L = [int(item) for item in input("Enter a list with spaces in between :").split()]
a = -1
checked = []
#a = a +L[a]
n = len(L)
for i in range (0,n):
    if L[i] not in checked:
        checked.append(L[i])
        a = a +1
        b = L[a]
    #print(b)
        test = L.count(b)
        test1 = b<1
    
        print(b, "occurs" , test, "amount of times")

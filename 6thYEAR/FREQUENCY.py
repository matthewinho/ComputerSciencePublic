def freq(L):
    check = []
    n = len(L)
    for i in range (0,n):
        if L[i] not in check:
            check.append(L[i])
            b = L[i]
            frequency = L.count(b)
            print(b, "occurs" , frequency, "amount of times")
 
 
Awns =freq(L)

#decimal TO BINARY	
def decimal():
    ba = []
    no = int(input("enter a number"))
    while no>0:

 
     a = no%2
     b = no//2
     no = b

     print(b, "remainder", a)
     ba.append(a)


 
    
    ba.reverse()
    #print(ba)

 
    
    return  ba
ans = decimal()
print(ans)
 
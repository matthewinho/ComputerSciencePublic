list1 =  [int(item) for item in input("Enter the list items with space between : ").split()]

Target = int(input("Enter Target Value"))

n = len(list1)
X = 0
TA = list1[X]
for  i in range(len(list1)) :
    X = X + 1 
    if X != Target:
        print("not target value")
    #if X == Target:
else:
        print( TA, " was found and the target value " , Target)
        

"""
L = [[2,5,0],[3,7,4],[1,6,9],[4,2,0]] #list within lists
print(L) #wholething
print(L[0]) #calls first set of numbers in list
# ROWS AND COLUMNS START AT 0 
# to print number 6
row6 = L[2][1]
print(row6)



#MY 2D DICTIONARY

D2  ={'John':{'N':3056 ,'S':8463,'E':8441,'W':2694},'Tom':{'N':3056 ,'S':8463,'E':8441,'W':2694}}


print(D2['John'])
print(D2['John']['N'])
"""



#1
L1 = [[2,5,0],[3,7,4],[1,6,9],[4,2,0]]

print(L1)

"""
x = int(input("select a row"))
y = int(input("select a column"))
a = L1[x][y]
#97
print(a)
"""

#98
"""
z=  int(input("what row would u like displayed?(0-3)"))

row = L1[z]
print("you picked row",z,"\n",row)

new = int(input("enter a value"))
row.append(new)
print(row)


#100


"""
#MY 2D DICTIONARY

D2  ={'John':{'N':3056 ,'S':8463,'E':8441,'W':2694},'Tom':{'N':4832 ,'S':6786,'E':4737,'W':3612},'Anne':{'N':5239 ,'S':4802,'E':5820,'W':1859},'Fiona':{'N':3904 ,'S':3645,'E':8821,'W':2451}}


#print(D2['John'])
#print(D2['John']['N'])
#print(D2['Anne']['W'])
test = input("enter a relevant name")
test1 = input("enter a relevant region (N,S,E,W)")
print(D2[test][test1])
print("LETS MAKE A CHANGE TO SOMEONES SALES FIGURE")
test2 = input("enter a relevant name AGAIN")
test3 = input("enter a relevant region AGAIN (N,S,E,W)")
change = D2[test2][test3]


print(D2[test2])
for i in range(4):
    a =  input("enter a name")
    

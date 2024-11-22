from random import randint 
#test = 3
u = 0
s = randint(1, 100)
points = 0
while (u != s):
    s = randint(1, 100)
    u = int(input("Enter your guess: "))
    d = u - s
    
    if d >= 30:
        print("you lose 30 points >:C")
        points = points - 30
        
    if d <= 20:
        print("You score 20 points" )
        points = points +20
    if s == u:
        print("JACKPOT")
        points = points +100
    print("you guessed", u, " the secret number is ", s ," with a difference of ",d)
    ans = input("DO YOU WISH TO CONTINUE (Y/N)")
    print("your total points currently is ", points)
    if 'Y' == ans:
        print("")
        
    else:
        ("GAME HAS ENDED")
        print("your total points currently is ", points)
        print(exit())




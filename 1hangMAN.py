import random
print ("LETS PLAY HANGMAN")
print("--------------------")

      
print("        ____ ")
print("       |    |")
print("            |")
print("            |")
print("            |")
print("            |")
print("            |")
print("            |")
print("    ________|")

#\n


score = 0
lives = 5
ca = []
#,"cat" ,"mouse" , "frog", "penguin"
print("THE THEME IS ANIMALS")
a = ["dog","cat" ,"mouse" , "frog", "snake" , "lion" , "tiger"]

index  =  list (random.choice(a))

#left = ("x", "x",)

#lol =[]
while True:
    
    l=len(index)
    prompt = str(l)+" letters in the word, guess what it is" 
    gu = input(prompt)
    lol = index.count(gu )
    ca.append(gu)
    
    print(ca, "guessed ")
    print(lives, "LIVES")
    if lol > 0  :
        print(" you have that letter in the word")
        #index.remove(gu)
        score = score +1
        print(score,"out of",l, "letters found")
    
        #print(l," words left")
    
    
        
    else:
        lives = lives - 1
        print("LETTER IS NOT IN WORD")
        print(lives , "lives left")
    if lives == 5:
       
      
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
        
    if lives == 4:
       
      
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("       |    |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 3:
       
      
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|    |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 2:
       
      
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 1:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("      /     |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
       
      
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    
    
    if lives == 0:
        print(" Game OVER ")
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("       |    |")
        print("      / \   |")
        print("            |")
        print(" imagine    |")
        print("    ________|")
        break
    if score == l:
        print("YOU HAVE GUSSED THE WORD,the word was", index," you win the man doesnt die")
        a = input("would you like to play again ? type YES or NO")
    if a == "NO":
        break
    if a == "YES":
        ("nah u cant i was joking")
        break
#if l == 0:
  #  print("you have won")
        
    #create a list of the word they are trying to guess
    #if they enter the correct letter, loop through th elist and remove each
    #occurance of that letter
    #if the len == 0 end

    

#  |
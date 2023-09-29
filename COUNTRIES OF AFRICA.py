




countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome &Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe" ]
#countries = ["Algeria", "Angola", "Benin"]
print("---Countries of AFRICA!---")
#P = 0 
score = 0
lives = 3
LI = ("lives left")
print("Number of countries to guess")
while len(countries) > 0:
    print(len(countries))
    print("YOUR SCORE")
    print(score)
    print("LIVES LEFT")
    print(lives)
    a = input("Enter a name of a country    ")

    if a in countries:
        print("Correct Guess")
        score =  score + 1
        countries.remove(a)
    else:
        print("INCORRECT GUESS")
        lives = lives -1
        print(lives,LI)
    if lives < 0 or lives == 0:
        print(" GAME OVER. TRY AGAIN")
        break

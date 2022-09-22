word = "EVAPORATE"

print("Welcom to Hangman!\n_ _ _ _ _ _ _ _ _")
result = "_ _ _ _ _ _ _ _ _"
done = True
while done:
    letter = input("Guess your letter: ")
    if result.find("_") == -1:
        print("You won!")
    else:
        if word.find(letter) != -1:
            
            print(result)
        else:
            print("Incorrect!")    


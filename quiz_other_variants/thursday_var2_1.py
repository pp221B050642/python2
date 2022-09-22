import random

number = random.randint(1, 100)
print(f"number: {number}")
guess1 = int(input())
if guess1>number:
    print("The number is fewer")
elif guess1<number:
    print("The number is more")    
else:
    print("BINGO!") 
    exit()
    
guess2 = int(input())
if guess2>number:
    print("The number is fewer")
elif guess2<number:
    print("The number is more")    
else:
    print("BINGO!") 
    exit()

guess3 = int(input())
if guess3>number:
    print("The number is fewer")
elif guess3<number:
    print("The number is more")    
else:
    print("BINGO!")
    exit()         

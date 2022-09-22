letter = str(input())

vowels = "euioa"
answer = False
for i in vowels:
    if letter == i:
        answer = True

if answer == True:
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")    
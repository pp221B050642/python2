#chinese zodiac sign

year = int(input())

zodiac = ["dragon", "snake", "horse", "ram", "monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "hare"]

for i in range(0, len(zodiac)):
    if (year-200)%12 == i:
        print(f"Your Chinese Zodiac Sign is {zodiac[i]}")
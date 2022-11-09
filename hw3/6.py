import re
#16 digit
#one number cannot be used more than3 times
#separeted only by "-"
#contains only digits
#starts with 4, 5, 6
n = int(input())
credit_cards = []
valid = r"\b(4|5|6)(\d{3})\-?(\d{4})\-?(\d{4})\-?(\d{4}\b)"
non_repeated = r'(\d)(-?\1){3}'
for i in range(n):
    number = input()
    credit_cards.append(number)

for card in credit_cards:
    if re.findall(valid, card):
        if re.findall(non_repeated, card):
            print("invalid")
        else:
            print("valid")
    else:
        print("invalid")




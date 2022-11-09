#valid mobile numbers
import re

valid = r'\+?(7|8)\s?\-?(777|747|701|705|702|775)\s?\-?(\d{3})\s?\-?(\d{2})\s?\-?(\d{2})'

n = int(input())

for i in range(n):
    mob_num = input()
    if re.findall(valid, mob_num):
        print("yes")
    else:
        print("no")
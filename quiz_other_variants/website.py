import re

passw = list(input().split())

for i in passw: 
    if len(i)>5 and len(i)<13:
        if re.search("[a-z]", i):
            if re.search("[A-Z]", i):
                if re.search("[0-9]", i):
                    if re.search("[$#@]", i):
                        print(i)

        
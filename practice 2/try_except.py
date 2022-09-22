#not finished
# string with first 2 chars and last 2 chars

s = input()

try:
    if type(s) is str or len(s)>2:
        s1 = s[0:2]
        s2 = s[-2:]
        print(s1+s2)
except len(s) == 2:
    print(s+s)
else:
    print(" ")


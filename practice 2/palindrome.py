#palindrome

s = str(input())

s1 = s[::-1]

if s == s1:
    print("yes")
else:
    print("no")    
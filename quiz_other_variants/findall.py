locations = []
def findall(s, c):
    global locations
    for i in range(len(s)):
        if s[i] == c:
            locations.append(i)
    return locations

s, c = input().split()

print(findall(s, c))
l  = [ 'cabaabca', 'aabaabac','aaabbcba', 'aabacbab', 'acababba']

users_string = input()

d = {}
result = []

for i in range(len(users_string)):
    if users_string[i] != "*":
        d[i] = users_string[i]
answer = True
for i in l:
    d1 = {}
    for j in range(len(i)):
        d1[j] = i[j]

    for k in d.keys():
        if d[k] != d1[k]:
            answer = False
    if answer == True:
        result.append(i)
    d1.clear()    

print(result)

    

    



# result = []
# for i in range(len(users_string)):
#     if users_string[i] != "*":
#         for j in l:
#             answer = True
#             for k in range(len(j)):
#                 if users_string[i] != j[k]:
#                     answer = False
#             if answer == True: result.append(j)                    

# print(result)
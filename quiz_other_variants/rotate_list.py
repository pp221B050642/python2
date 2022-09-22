user_input = input()
result_list = []
for i in range(len(user_input)):
    if i<len(user_input)-1:
        result_list.append(user_input[i])
    if i==len(user_input)-1:
        result_list.insert(0, user_input[i])
result = ""
for i in result_list:
    result += i
print(str(result))
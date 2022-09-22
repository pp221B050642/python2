#sum and average

user_input = list(input().split())
sum = 0
for i in user_input:
    if i == 0:
        break
    else:
        sum+=int(i)
average = sum/(len(user_input)-1)

print(f"The sum is equal to {sum} \nThe average is equal to {average}")
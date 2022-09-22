#secret code

message = str(input())
n = int(input())

for i in range(n):
    for j in range(len(message)):
        if i == (j % n):
            print(message[j], end = " " )


# s = str(input())

# n = int(input())

# def create_groups(s, n):
#     x = 0
#     for i in range(0, n):
#         i = s[x::n]
#         print(i)
#         x += 1
           
# print(create_groups(s, n))
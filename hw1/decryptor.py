
code = list(str(input()). split(" "))
n = int(input())

for i in range((len(code)// n)+(len(code)%n)):
    for j in range(len(code)):
        if i == ((j % ((len(code) // n)+1))):
           print(code[j], end = " " )

variables = list(input().split())

variables.sort()
length = int(len(variables)/2)
median = float(variables[length])
print(f"The median is {median}")

#create a program that takes a list of numbers and return the number that's unique
#3 3 3 7 3 -> 7
#0 0 0 0.77 0 0 -> 0.77
#0 1 1 1 1 1 -> 0

def function(list):
    d = {}
    for i in list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key in d.keys():
        if d[key] == 1:
            print(key)            

array = list(input().split())

function(array)
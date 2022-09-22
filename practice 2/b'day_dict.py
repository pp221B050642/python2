d = {
    "Adel" : "25.01.04", 
    "Ayazhan" : "29.01.04", 
    "Zhanar"  : "05.09.1975"
}

s = str(input())

if s in d.keys():
    print(s +"'s birthday is " + d[s])
else:
    print("We don't have data about " + s)   
               


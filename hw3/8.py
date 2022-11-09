import re

initials = input()

with open("namelist.txt", "r+") as nl:
    all = nl.read().split("\n")
    for person in all:
        name=person.split()
        for i in name:
            for j in i:
                if len(initials) == 2:
                    if j[0] == initials[0] and j[-1] == initials[1]:
                        print(person)
                elif len(initials) == 3:
                    if j[0] == initials[0] and j[1] == initials[1] and j[2] == initials[2]:
                        print(person)





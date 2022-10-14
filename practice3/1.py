import re

with open("file.txt", "r") as the_file:
    all = the_file.read().split("\n")
    for student in all:
        each = student.split()
        if int(each[1]) >= 50 and int(each[2]) >= 50 and int(each[3]) >= 50:
            print(each[0])
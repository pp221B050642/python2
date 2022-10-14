import re

with open("logfile.txt", "r") as the_file:
    all = the_file.read().split("\n")
    for user in all:
        each = user.split(", ")
        time1 = each[1].split(":")
        time2 = each[2].split(":")
        if int(time1[0])>int(time2[0]):
            if int(time1[1])>=int(time2[1]):
                print(each[0])
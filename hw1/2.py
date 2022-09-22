#print "R"

letter_r = ""
for i in range(0, 7):
    for j in range(0, 6):
        if (i == 0 or i == 3) and (j>-1 and j<4) or ((i>0 and i<3) and (j==0 or j==4)) or j == 0 or (i == 4 or i == 5 or i == 6) and (j == i-2):
            letter_r += "*"       
        else:
            letter_r += " "   
    letter_r+="\n"
print(letter_r)
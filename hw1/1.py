#print "O"
letter_o = ""
for i in range(0, 7):
    for j in range(0, 6):
        if i == 0 and (j>0 and j<5):
            letter_o += "*"   
        elif (i>0 and i<6) and (j==0 or j==5):
            letter_o += "*" 
        elif i==6 and (j>0 and j<5):
            letter_o += "*" 
        else:
            letter_o += " "   
    letter_o+="\n"
print(letter_o)

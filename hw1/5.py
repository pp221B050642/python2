month = str(input())

days30 = ["April", "June", "September", "November"] 

if month == "February":
    print("28/29 days")
elif month in days30:
    print("30 days")    
else:
    print("31 days")    

months = {
    "01": "January",
    "02": "February", 
    "03" : "March", 
    "04" : "April", 
    "05" : "May", 
    "06" : "june",
    "07" : "July", 
    "08" : "August", 
    "09" : "September", 
    "10" : "October", 
    "11" : "November", 
    "12" : "December"
}

month = input()
day = int(input())
answer = "winter"
m = months[month]
if month == "03" or month =="04" or month == "05":
    answer = "spring"
    print(f"{m}, {day}. Season is {answer}") 
elif month == "06" or month =="07" or month == "08":
    answer = "summer"
    print(f"{m}, {day}. Season is {answer}") 
elif month == "09" or month =="10" or month == "11":
    answer = "autumn"
    print(f"{m}, {day}. Season is {answer}")   
else:
    print(f"{m}, {day}. Season is {answer}")    


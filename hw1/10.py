#zodiac signs

day = int(input())
month = str(input())

if month == "January":
    if day < 20:
        zodiac_sign = "Capricorn"
    else:
        zodiac_sign = "Aquarius"
elif month == "February":
    if day < 19:
        zodiac_sign = "Aquarius"
    else:
        zodiac_sign = "Pisces"
elif month == "March":
    if day < 21:
        zodiac_sign = "Pisces"
    else:
        zodiac_sign = "Aries"
elif month == "April":
    if day < 20:
        zodiac_sign = "Aries"
    else:
        zodiac_sign = "Taurus"
elif month == "May":
    if day < 21:
        zodiac_sign = "Taurus"
    else:
        zodiac_sign = "Gemini"
elif month == "June":
    if day < 21:
        zodiac_sign = "Gemini" 
    else:
        zodiac_sign = "Cancer"
elif month == "July":
    if day < 23:
        zodiac_sign = "Cancer"
    else:
        zodiac_sign = "Leo"
elif month == "August":
    if day < 23:
        zodiac_sign = "Leo"
    else:
        zodiac_sign = "Virgo"
elif month == "September":
    if day < 23:
        zodiac_sign = "Virgo"
    else:
        zodiac_sign = "Libra"
elif month == "October":
    if day < 23:
        zodiac_sign = "Libra"
    else:
        zodiac_sign = "Scorpio"
elif month == "November":
    if day < 22:
        zodiac_sign = "Sorpio"
    else:
        zodiac_sign = "Sagittarius"
elif month == "December":
    if day < 22:
        zodiac_sign = "Sagittarius"
    else:
        zodiac_sign = "Capricorn"                                                    

print(f"Your Zodiac sign is {zodiac_sign}")

import datetime

months =  {"JAN":1, "FEB" : 2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7 ,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12}

day, month, year = input("Enter the date in format(DD-MMM-YYYY)\n").split("-")

month = months[month]

day = int(day)
year = int(year)

print("%.2d-%.2d-%.4d"%(day, month, year))
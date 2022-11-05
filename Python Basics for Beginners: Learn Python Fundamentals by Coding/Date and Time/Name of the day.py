from datetime import datetime
from datetime import  timedelta

month, day, year = map(int, input("Enter the date as mm/dd/yyyy format:\n").split("/"))

n = int(input())

date = datetime(year, month, day)

date = date + timedelta(n)

day = date.strftime("%A")

print("The day is :",day)
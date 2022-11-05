year = int(input())

years = (year - 1) -1900

leapYears = years // 4

nonLeapYears = years - leapYears

noOfDays = (nonLeapYears * 365) + (leapYears * 366)  + 1 

day = noOfDays % 7

days = ["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(days[day])
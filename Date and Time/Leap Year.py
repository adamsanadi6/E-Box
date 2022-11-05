import calendar

date = input("Enter the date in format(dd/mm/yyyy)\n")
yyyy = int(date[6:])
if calendar.isleap(yyyy) :
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
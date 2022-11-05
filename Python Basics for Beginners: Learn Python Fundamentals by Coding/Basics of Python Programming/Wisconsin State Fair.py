salary = int(input("Enter the total salary paid\n"))
weekend = 0
for i in range(10, salary+1):
    x = i * 80 + (i - 10) * 50
    if(salary - x >= 0 and salary - x < 130):
        weekend = i - 10;
        break
print("Number of weekday hours is " + str(weekend + 10))
print("Number of weekend hours is " + str(weekend))
number_of_people = int(input("Enter the total number of people\n"))
first_day = 0
second_day = 0
third_day = 0
for i in range(number_of_people+1):
    if(first_day + second_day + third_day == number_of_people):
        break
    first_day += 1
    second_day = 2 * first_day
    third_day = first_day // 2
print("Number of attendees on day 1 : " + str(first_day))
print("Number of attendees on day 2 : " + str(second_day))
print("Number of attendees on day 3 : " + str(third_day))
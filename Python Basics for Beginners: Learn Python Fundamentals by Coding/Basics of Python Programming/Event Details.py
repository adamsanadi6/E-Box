name_of_event = input("Enter the name of the event\n")[: 50]
type_of_event = input("Enter the type of the event\n")[:50]
number_of_people = int(input("Enter the number of people expected\n"))
is_it_paid = input("Is it a paid entry? (Type Y or N)\n")[:1]
projected_expenses = float(input("Enter the projected expenses (in lakhs) for this event\n"))
projected_expenses = "{0: .1f}".format(projected_expenses)
print("Event Name : " + name_of_event + "\nEvent Type : " + type_of_event )
print("Expected Count : " + str(number_of_people) + "\nPaid Entry : " + is_it_paid )
print("Projected Expense : " + str(projected_expenses) + "L")
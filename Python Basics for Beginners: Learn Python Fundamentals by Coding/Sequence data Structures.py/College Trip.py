n = int(input())
madikeri = mysore = manglore = invalid = 0
for i in range(n):
    vote = int(input())
    if vote == 1:
        madikeri += 1
    elif vote == 2:
        mysore += 1
    elif vote == 3:
        manglore += 1
    else:
        invalid += 1

print(str(madikeri) + "\n" + str(mysore) + "\n" + str(manglore) + "\n" +str(invalid))

if madikeri > mysore and madikeri > manglore:
    print("Madikeri")
elif mysore >madikeri and mysore > manglore:
    print("Mysore")
elif manglore > madikeri and manglore > mysore:
    print("Mangalore")
else:
    print("Trip cancelled")
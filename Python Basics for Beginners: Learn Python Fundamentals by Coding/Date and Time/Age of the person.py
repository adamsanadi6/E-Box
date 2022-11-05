birthDate = input("Enter Birth date as mm/dd/yyyy format:\n")
currentDate = input("Enter Current date as mm/dd/yyyy format:\n")

bmm  = int(birthDate[:2])
bdd     = int(birthDate[3:5])
byyyy = int(birthDate[6:])

cmm = int(currentDate[:2])
cdd = int(currentDate[3:5])
cyyyy = int(currentDate[6:])

age = cyyyy - byyyy

if cmm < bmm:
    age -= 1
elif cmm == bmm:
    if bdd > cdd:
        age -= 1

print("The current age of the person is %d"%age)
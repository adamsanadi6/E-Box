loop = True
records = dict()
EmpId = list()
print("1] Create a Record\n2] Display Records\n3] Update Records\n4] Exit")
while loop:
    choice = int(input("Enter your choice :\n"))
    if choice == 1:
        name = input("Enter name of employee :\n")
        empId = input("Enter emp id :\n")
        EmpId.append(empId)
        records[empId] = name
    elif choice == 2:
        for key in sorted(EmpId):
            print("%d-%s"%(int(key), records[key]))
    elif choice == 3:
        key = input("Enter employee id to update :\n")
        records[key] = input("Enter new name of emplyee to update :\n")
    elif choice == 4:
        loop = False
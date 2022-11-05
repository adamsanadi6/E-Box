n = int(input("Enter the no donors available\n"))

donors = dict()

for i in range(1, n + 1):
    print("Enter the details of donor %d\n"%i)
    name = input()
    email = input()
    phoneNumber = input()
    bloodGroup = input()
    donors[bloodGroup] = [name, email, phoneNumber]
    # print(donors[bloodGroup])

bloodGroup = input("Enter the required blood group\n")

if bloodGroup not in donors:
    print("No donor with required blood group")
else:
    print("Details of matched donor\n%s\n%s\n%s\n%s"%(donors[bloodGroup][0], donors[bloodGroup][1], donors[bloodGroup][2], bloodGroup))
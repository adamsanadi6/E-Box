with open("file.txt", "r") as txtFile:
    donor = 1
    bloodGroup = input("Enter blood group to search\n")
    line = list(txtFile.readline().split(","))
    print("Donor details")
   
    while len(line) == 3:
        if line[1] == bloodGroup:
            print("Donor",donor)
            print("Donor name :",line[0])
            print("Blood group :",bloodGroup)
            print("Donor location :",line[2])
            donor += 1
        line = list(txtFile.readline().split(","))
with open("sample.txt", "r") as sample:
    numbers =[int(i) for i in sample.readlines()]
    numbers.sort()
    print("Ascending Order of the file content is:")
    for i in numbers:
        print(i)
with open("sample.txt", "r") as sample:
    numbers = sample.readlines()
    total = 0
    for i in numbers:
        total += int(i)
    print("The sum of the integers in the file sample.txt is:", total)
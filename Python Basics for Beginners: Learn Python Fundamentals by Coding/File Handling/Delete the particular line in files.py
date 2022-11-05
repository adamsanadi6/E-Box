n = int(input("Enter line number of the line to be deleted:\n"))
with open("input.txt", "r") as inputFile:
    with open("output.txt", "w") as outputFile:
        count = 1
        line = inputFile.readline()
        while len(line) >= 0:
            if count == n:
                break
            outputFile.write(line)
            count += 1
            line = inputFile.readline()
        lines = inputFile.readlines()
        outputFile.writelines(lines)
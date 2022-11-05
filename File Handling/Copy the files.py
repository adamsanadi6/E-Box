with open("input.txt", "r") as inputFile:
    with open("output.txt", "w") as outputFile:
        lines = inputFile.readlines()
        outputFile.writelines(lines)
with open("input.txt", "r") as inputFile:
    with open("output.txt", "w") as outputFile:
        lines = inputFile.readline()
        String = list()
        while len(lines) > 0:
            outputFile.write(lines[-2::-1] + "\n")
            
            lines = inputFile.readline()
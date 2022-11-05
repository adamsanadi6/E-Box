with open("input.txt", "r") as inputFile:
    with open("output.txt", "w") as outputFile:
        line = inputFile.readline()
        while len(line) > 0:
            li = list(line)
            n = len(li)
            for i in range(n):
                if li[i] == " ":
                    if li[i + 1].islower():
                        li[i+1] = li[i+1].upper()
            li = "".join(li)
            outputFile.write(li)
            line = inputFile.readline()
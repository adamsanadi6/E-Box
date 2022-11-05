with open("input.txt", "r") as inputFile:
    line = inputFile.readline()
    function =[]
    while len(line) > 0:
        method = ""
        if line[len(line) - 2] == ')':
            words = (line.split()[1])
            for i in range(len(words)):
                if words[i] == '(':
                    break
                method = method + words[i]
            print(method)
        line = inputFile.readline()
def printValue(num, den):
    if num % den == 0:
        print(num // den)
    elif num < den:
        for i in range(den, 1, -1):
            if num % i == 0 and den % i == 0:
                num = num // i
                den = den // i
        print("%d/%d"%(num, den))
    else:
        wholeNumber = num // den
        reminder = num - (wholeNumber * den)
        for i in range(num, 1, -1):
            if reminder% i == 0 and den % i == 0:
                reminder = reminder // i
                den = den // i
        print("%d %d/%d"%(wholeNumber, reminder, den))

num = int(input())
den = int(input())
printValue(num, den)
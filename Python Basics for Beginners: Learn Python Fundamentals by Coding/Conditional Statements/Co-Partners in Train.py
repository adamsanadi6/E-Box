n = int(input())

if n%8 == 0:
    print("%dSL"%(n - 1))
elif n%8 == 7:
    print("%dSU"%(n + 1))
elif n%8 == 6:
    print("%dUB"%(n - 3))
elif n%8 == 5:
    print("%dMB"%(n - 3))
elif n%8 == 4:
    print("%dLB"%(n - 3))
elif n%8 == 3:
    print("%dUB"%(n + 3))
elif n%8 == 2:
    print("%dMB"%(n + 3))
else:
    print("%dLB"%(n + 3))
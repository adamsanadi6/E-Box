#!/usr/bin/python

def findType( x ):
    #code here
    sum = 0
    for i in range(1, (x // 2) + 1):
        if x % i == 0:
            sum += i
    if sum < x:
        return 1
    elif sum > x:
        return -1
    return 0

x=int(input())
res = findType(x)
if res == 0:
     print("%d is a perfect number"%x)
elif res == 1:
    print("%d is a deficient number"%x)
else:
    print("%d is an abundant number"%x)
#!/usr/bin/python

def findType( x ):
    #type your code here
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    if count == 4:
        return 1
    return 0
    
x=int(input())
#type your code here
res = findType(x)
if res == 1:
    print("Nice")
else:
    print("Not Nice")
def findValue(f1, f2):
    if f1 > f2:
        f2, f1 = f1, f2
    for i in range(f1, 1, -1):
        if f1 % i == 0 and f2 % i == 0:
            return i
 
    return 1

f1 = int(input())
f2 = int(input())
print(findValue(f1, f2))
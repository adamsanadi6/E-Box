n = int(input())

even, odd = 0, 0
for i in range(n):
    if (int(input()) % 2 == 0):
        even += 1
    else:
        odd += 1

print("%d %d"%(even, odd))
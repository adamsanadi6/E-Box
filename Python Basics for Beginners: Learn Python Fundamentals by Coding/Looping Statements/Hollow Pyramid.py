n = int(input())
k = 0
for i in range(n):
    if i == n-1:
        print("*"*((2*n)-1))
        break
    for j in range (n - i - 1):
        print("b",end="")
    print("*", end = "")
    for j in range(k):
        print("i", end= "")
    if i == 0:
        k += 1
    else:
        k += 2
    if i != 0:
        print("*", end = "")
    for j in range(n - i - 1):
        print("b", end = "")
    print()
def find(n):
    for i in range(1, n+1):
        if ((i * (i + 1))/2) == float(n):
            return 1
    return 0

if find(int(input())) == 1:
    print("Yes")
else:
    print("No")
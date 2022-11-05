n  = int(input())

ratio = list(map(int, input().split()))

maximum = max(ratio)

for i in range(maximum + 1, 1, -1):
    flag = True
    for j in range(len(ratio)):
        if ratio[j] % i != 0:
            flag = False
            break
    if flag:
        for j in range(len(ratio)):
            ratio[j] = ratio[j] // i
for i in ratio:
    print(i, end=" ")
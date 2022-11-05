n = int(input())
ids = list(map(int, input().split()))

ids.sort()

for i in range(0, n, 2):
    if i == n -1:
        print(ids[i])
    else:
        if ids[i] != ids[i + 1]:
            print(ids[i])
            break
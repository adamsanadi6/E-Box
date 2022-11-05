n = int(input())

colors = list(map(int, input().split()))
colors.sort()
col = colors[0]
counts = colors.count(col)
k = counts
if k == n:
    print(0)
else:
    i = k
    while i < n:
        temp = colors[i]
        k = colors.count(temp)
        if k > counts:
            counts = k
            col = temp
        i += k
    print(n - counts)
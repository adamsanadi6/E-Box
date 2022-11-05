n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = prev = 0

for i in range(n):
    if a[i] - prev >= b[i]:
        count += 1
    prev = a[i]
print(count)
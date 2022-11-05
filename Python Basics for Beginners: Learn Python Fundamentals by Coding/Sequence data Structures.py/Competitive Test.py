n = int(input())
a= list(map(int, input().split()))

count = n

for i in range(n):
    for j in range(i , n-1):
        if a[j] <= a[j +1]:
            count += 1
        else:
            break
print(count)
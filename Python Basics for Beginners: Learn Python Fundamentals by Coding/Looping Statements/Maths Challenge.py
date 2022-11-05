k = int(input())
N = int(input())
n =2
multiplier = 1
count = 0
n2 = n
while n <= N:
    if n2 % multiplier != 0:
        if multiplier - 1 == k:
            count += 1
        multiplier = 1
        n += 1
        n2 = n
        continue
    n2 += 1
    multiplier += 1
print(count)
N = int(input())
count = 0
if N > 99:
    count += (N // 100)
    N = N % 100
if N > 49:
    count += (N // 50)
    N = N % 50
if N > 9:
    count += (N // 10)
    N = N % 10
if N > 4:
    count += (N // 5)
    N = N % 5
if N > 1:
    count += (N // 2)
    N = N %2
if N > 0:
    count += N

print(count)
def fiboLastDigit(prev1, prev2, n):
    if n == 1:
        return 1
    return prev1 + fiboLastDigit(prev1 + prev2, prev1, n - 1)

num = int(input())
if num == 0:
    print(0)
elif num == 1:
    print(1)
else:
    print(fiboLastDigit(1, 0, num - 1)%10)
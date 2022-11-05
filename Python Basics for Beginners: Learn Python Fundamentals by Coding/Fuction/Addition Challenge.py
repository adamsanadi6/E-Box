def finSum(n):
    sum = 0
    for i in range(0, n + 1):
        sum += 2 ** i
    return sum

print(finSum(int(input())))
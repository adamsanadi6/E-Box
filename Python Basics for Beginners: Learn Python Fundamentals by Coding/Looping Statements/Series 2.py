n = int(input())

sum = 20
diff = 40
print(sum, end = " ")

for i in range(0, n-1):
    sum += diff
    diff += 4
    print(sum, end = " ")
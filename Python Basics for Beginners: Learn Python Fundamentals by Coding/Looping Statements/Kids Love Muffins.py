n, k = map(int, input().split())

muffines = list(map(int, input().split()))

result = 0

for i in muffines:
    result = result + (i // k)

print(result)
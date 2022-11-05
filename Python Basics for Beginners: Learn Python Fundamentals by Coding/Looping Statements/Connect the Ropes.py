n, k = map(int, input().split())

ropes = list(map(int, input().split()))

result = sum(ropes)

for i in range(n-1):
    result -= (2 * k)
    
print(result)
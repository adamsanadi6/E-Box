n, k = map(int, input().split())
result = ["No"] * n
print(result)
extinct = list(input().split())
print(extinct)
for i in range(k):
    setences = list(input().split())
    print(setences)
    for j in range(n):
        if extinct[j] in setences:
            result[j] = "Yes"
    print(result)

for i in result:
    print(i, end=" ")
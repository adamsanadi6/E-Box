n, m = map(int, input().split())

result = "Yes"

if (n+m) % 2 == 0 and (n % 2 != 0 or m % 2 != 0):
    result = "No"
print(result)
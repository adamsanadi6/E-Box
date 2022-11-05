s = input()
Set = set(s)
result = "No"
for i in Set:
    maxi = s.count(i)
    if maxi + maxi == len(s):
        result = "Yes"

print(result)
x = input()
y = input()

lenX = len(x)
lenY = len(y)

result = "Yes"
if lenX != lenY:
    result = "No"
else:
    for i in range(lenX):
        if x[i] == y[i] or x[i] == '?' or y[i] == '?':
            continue
            result = "No"
            break

print(result)
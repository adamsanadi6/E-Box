x = input()
y = input()

n = len(x)
z=""
for i in range(n):
    if x[i] != y[i]:
        z += 'B'
    elif x[i] == 'B':
        z += 'W'
    else:
        z += 'B'
print(z)
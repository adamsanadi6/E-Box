n = int(input())

sticks = list(map(int, input().split()))

newStick = 0

for i in range(0, len(sticks) - 1, 2):
    if sticks[i] <= sticks[i + 1]:
        newStick += sticks[i]
    else:
        newStick += sticks[i + 1]

print(newStick)
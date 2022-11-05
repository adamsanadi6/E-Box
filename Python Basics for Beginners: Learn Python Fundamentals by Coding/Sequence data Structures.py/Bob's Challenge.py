n = int(input())
sticks = list(map(int, input().split()))
li = []

for i in sticks:
    count = sticks.count(i)
    if count > 1:
        count = count // 2
        for j in range(count):
            li.append(i)
        while i in sticks:
            sticks.remove(i)

li.sort(reverse = True)
if len(li) > 1:
    print(li[0] * li[1])
else:
    print(-1)
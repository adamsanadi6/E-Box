n = int(input())

problems = list(map(int, input().split()))

summ = sum(problems)

avg = summ // n

delete = summ - (avg * n)
print(delete, end = " ")
moves = 0

problems.sort(reverse = True)

for i in range(len(problems)):
    if delete == 0:
        break
    if problems[i] == avg:
        continue
    if problems[i] > avg and delete!= 0:
        temp = problems[i] - avg
        if temp >= delete:
            delete = 0
            problems[i] -= delete
        else: 
            delete -= (problems[i] - avg)
            problems[i] = avg

problems.sort(reverse = True)

for i in range(len(problems)):
    if problems[i] < avg:
        temp = avg - problems[i]
        moves += temp
        for j in range(0, i):
            if temp == 0:
                break
            if problems[j] >= avg:
                temp2 = problems[j] - avg
                if temp > temp2:
                    temp -= temp2
                    problems[j] = avg
                else:
                    temp = 0
                    problems[j] -= temp
print(moves)
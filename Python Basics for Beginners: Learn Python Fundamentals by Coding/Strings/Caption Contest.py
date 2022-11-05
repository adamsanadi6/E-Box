s1 = input()
s2 = input()

n = len(s1)
maximum = minimum = 0
for i in range(n):
    if s1[i] == '?' or s2[i] == '?' :
        maximum += 1
    elif s1[i] != s2[i]:
        maximum += 1
        minimum += 1

print(minimum, maximum)
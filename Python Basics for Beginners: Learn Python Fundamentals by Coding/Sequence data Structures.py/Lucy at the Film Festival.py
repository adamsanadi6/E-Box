n = int(input())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
maxi = temp = 0
for i in range(n):
    if l[i] * r[i] > maxi:
        maxi = l[i] * r[i]
        temp = i
    elif l[i] * r[i] == maxi and l[i] < l[temp]:
        temp = i
print(temp + 1)
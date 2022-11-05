grades = list(map(int, input().split()))
avg = float("{0: .2f}".format(sum(grades)/5))
if 5  in grades and (avg >= 4.0) and 2 not in grades:
    print("Yes")
else:
    print("No")
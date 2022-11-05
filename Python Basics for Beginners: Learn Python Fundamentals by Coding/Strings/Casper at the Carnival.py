n= int(input())
casper = list(input().split())

flag = "Yes"
if casper[n - 1] == "cookie":
    flag = "No"
else:
    for i in range(n-1):
        if casper[i] == "cookie" and casper[i + 1] == "cookie":
            flag = "No"
            break
print(flag)
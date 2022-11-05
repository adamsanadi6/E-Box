d, c, l = map(int, input().split())
min = d 
max = d + c 
if c > d*2:
    min += ((c - (2* d)))

if l%2 != 0 or 2*min > l or 2*max < l:
    print("no")
else:
    print("yes")
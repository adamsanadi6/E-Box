a, b = map(int, input().split())
max = a + b
min = a
if a < b:
    min = b
if(min > max):
    min,  max = max, min
print("%d %d"%(min, max))
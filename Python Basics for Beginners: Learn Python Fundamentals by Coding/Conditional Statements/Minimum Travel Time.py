import math
n, v1,  v2 = map(int, input().split())
t1 = (math.sqrt(2)*n)*v1
t2 = (n*v2)
if t1 < t2 :
    print("Elevator")
else:
    print("Stairs")
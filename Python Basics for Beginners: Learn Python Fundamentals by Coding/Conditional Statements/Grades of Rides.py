hurlFactor, spinFactor, speedFactor = map(int, input().split())
condition1 = hurlFactor > 50
condition2 = spinFactor > 60
condition3 = speedFactor > 100
if condition1 and condition2 and condition3:
    print(10)
elif condition1 and condition2:
    print(9)
elif condition2 and condition3:
    print(8)
elif condition3 and condition1:
    print(7)
elif condition1 or condition2 or condition3:
    print(6)
else:
    print(5)
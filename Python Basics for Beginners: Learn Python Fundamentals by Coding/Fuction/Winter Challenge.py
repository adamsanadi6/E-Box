def findValue(x, y): 
    for n in range(1, y):
        if (x * n) % y == 1:
            return n
    return -1

inputs = input()

x = 0
if inputs != "Test Script - T5":
    x= int(inputs)
else:
    x = int(input())
m = int(input())

print(findValue(x, m))
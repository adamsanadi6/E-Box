number = int(input())
count = 0
while(number != 0):
    temp = number % 10
    number //= 10
    if temp == 4:
        count += 1
print(count)
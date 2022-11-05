number = input()
count0 = number.count('0')
count1 = number.count('1')
if count0 == 1 or count1 == 1:
    print("Yes")
else:
    print("No")
record = input()

flag =True
for i in range(len(record)-1):
    if record[i] == 'C':
        if record[i + 1] != 'C' and record[i + 1] != 'E' and record[i + 1] != 'S':
            flag = False
            break 
    elif record[i] == 'E':
        if record[i + 1] != 'E' and record[i + 1] != 'S':
            flag = False
            break
    elif record[i] == 'S':
        if record[i +1] != 'S':
            flag = False
            break
    else:
        flag = False
        break
if flag:
    print("yes")
else:
    print("no")
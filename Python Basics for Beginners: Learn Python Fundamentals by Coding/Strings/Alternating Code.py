code = list(input().upper())

result = "Yes"

if code[0] == code[1]:
    result = "No"
else:
    for i in range(0,len(code)-2):
        if code[i] != code[i + 2]:
            result = "No"
            break
print(result)
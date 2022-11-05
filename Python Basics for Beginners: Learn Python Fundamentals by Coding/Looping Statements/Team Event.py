n = int(input())

if n < 10:
    print("Invalid Input")
else:
    last = n % 10
    first = int(str(n)[0])
    print(abs(last - first))
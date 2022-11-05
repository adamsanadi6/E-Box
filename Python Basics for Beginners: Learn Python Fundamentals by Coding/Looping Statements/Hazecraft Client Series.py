def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
    return True



n = int(input())
start = 0
count = 0
while(count != n):
    if(isPrime(start)):
        count += 1
        print(start, end = " ")
    start += 1
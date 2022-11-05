n, m, k = map( int, input().split())

while k > 0:
    if m > n:
        m -= 1
    else:
        n -= 1
    k -= 1
print(abs(m - n))
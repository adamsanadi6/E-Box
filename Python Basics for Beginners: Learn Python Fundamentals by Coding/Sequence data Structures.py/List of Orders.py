from datetime import date
n = int(input())

orders =[]

for i in range(n):
    tup = tuple(input().split(","))
    orders.append(tup)

day, month, year = map(int, input().split("-"))
filterDate = date(year, month, day)
print(orders)
for i in range(n):
    d, m, y = map(int, orders[i][1].split("-"))
    departureDate = date(y, m, d)
    if departureDate > filterDate:
        print(orders[i][0])
def printPlanDetails(day, evening, night):
    a, b = 0, 0
    if day > 100:
        a = 0.25 * (day - 100)
    a += (0.15 * evening) + (0.20 * night)
    if day > 250:
        b = (0.45 * (day - 250))
    b += (0.35 * evening) + (0.25 * night)
    a = round(a, 2)
    b = round(b, 2)
    plans = [a, b]
    return plans

day = int(input())
evening = int(input())
night =int(input())

tup = printPlanDetails(day, evening, night)

print("Plan A costs %.2f"%tup[0])
print("Plan B costs %.2f"%tup[1])
if tup[0] == tup[1]:
    print("Plan A and B are the same price")
elif tup[0] > tup[1]:
    print("Plan B is cheapest")
else:
    print("Plan A is cheapest")
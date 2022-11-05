n = int(input())
m = int(input())

vehicals =[]

for i in range(n):
    regNo = input()
    chassisNo = input()
    engineNo = input()
    ownerName = input()
    address = input()
    details = [regNo, chassisNo, engineNo, ownerName, address]
    vehicals.append(details)

print("Reg.no: chassis no: engine no: owner name: address:")
i = 0
if m > len(vehicals):
    m = len(vehicals)
while i < m:
    print("%s %s %s %s %s"%(vehicals[i][0], vehicals[i][1], vehicals[i][2], vehicals[i][3], vehicals[i][4]))
    i += 1
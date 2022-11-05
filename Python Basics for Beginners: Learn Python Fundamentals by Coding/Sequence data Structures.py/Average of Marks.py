n = int(input())

record = dict()

for i in range(n):
    ip = list(input().split(" "))
    maths = float(ip[1]) 
    physics = float(ip[2])
    chemistry = float(ip[3])
    avg = "{0:.2f}".format((maths + physics + chemistry)/3)
    record[ip[0]] = avg

key = input()
print("Average Mark of is : %s"%record[key])
present = int(input())
future = int(input())

for i in range(present, future + 1, 60):
    print("All positions change in year %d"%i)
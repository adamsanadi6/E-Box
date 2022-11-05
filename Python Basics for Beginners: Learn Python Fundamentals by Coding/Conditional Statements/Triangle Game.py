angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("Prize 3")
elif angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Prize 2")
    else:
        print("Prize 1")
else:
    print("No Prize")
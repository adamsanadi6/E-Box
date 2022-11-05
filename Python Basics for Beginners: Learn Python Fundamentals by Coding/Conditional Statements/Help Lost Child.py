x1, y1, x2, y2 = map(int, input().split())

if  (x1 == x2 and y1 == y2) or (x1 != x2 and y1 != y2):
    print("sad")
else:
    if x2 > x1:
        print("right")
    elif x1 > x2:
        print("left")
    elif y1 > y2:
        print("down")
    elif y2 > y1:
        print("up")
side = int(input("Enter the side in cm of a square tile\n"))
n = int(input("Enter the number of square tiles available\n"))
m = 0
i = 1
while i*i <= n :
    m = i * i
    i += 1
area = m * side * side
print("Area of the largest possible square is " + str(area) + "sqcm")
x = int(input("Enter the value of X\n"))
y = int(input("Enter the value of Y\n"))
children = (y - (5 * x)) // 13
print("Number of children tickets sold : " + str(children))
print("Number of adult tickets sold : " + str(children + x))
print("Number of senior tickets sold : " + str(2 * children))
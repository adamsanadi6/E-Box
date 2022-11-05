m = int(input("Enter m\n"))
n = int(input("Enter n\n"))
minimum = 1
if(m == 1 and n == 1):
    minimum = 0
elif(m == 1):
    minimum = n - 1
elif(n == 1):
    minimum = m - 1
else:
    minimum = (m * n)  - 1
print("Minimum number of times is " + str(minimum))
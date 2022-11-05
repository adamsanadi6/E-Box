n = int(input())
# print(30, end = " ")
# print(35, end = " ")
# lastodd = 30
# lasteven = 35
# odd= 5
# even = 13
# for i in range(0, n-2):
#     if i % 2 == 0:
#         odd += (-2)
#         lastodd = lasteven + odd
#         print(lastodd, end = " ")    
#     else:
#         lasteven =lastodd +  even
#         if i==1:
#             lasteven = 41
#         even += 2
#         print(lasteven, end = " ")

series = [5, 3]
k = 1
k2 = 10
for i in range(n-3):
    if i % 2== 0:
        series.append(series[i] - (2 * k))
        k += 1
    else:
        series.append(series[i] + k2)
        k2 += 2
value = 30
k = 0
for i in range(n):
    print(value, end=" ")
    if i == n - 1:
        break
    value += series[k]
    k += 1
# print(series)
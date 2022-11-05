import math

range= int(input())

eventCoordinator = list(map(int, input().split()))
securityChief = list(map(int, input().split()))
crowdControlChief = list(map(int, input().split()))

d1 = abs(abs(eventCoordinator[0] - securityChief[0]) + abs(eventCoordinator[1] - securityChief[1]))
d2 = abs(abs(eventCoordinator[0] - crowdControlChief[0])+abs(eventCoordinator[1] - crowdControlChief[1]))
d3 = abs(abs(crowdControlChief[0] - securityChief[0]) + abs(crowdControlChief[1] - securityChief[1]))
if (d1<=range and (d2 <= range or d3 <= range)) or (d2<= range and d3 <= range):
    print("Yes")
else:
    print("No")
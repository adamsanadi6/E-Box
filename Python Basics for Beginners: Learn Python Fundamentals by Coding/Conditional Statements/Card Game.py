card1 = list(input().split())
card2 = list(input().split())
card3 = list(input().split())


if (card1[0] == card2[0] and card1[0] == card3[0]) and (card1[1] == card2[1] and card1[1] == card3[1]):
    print("Double Bonanza")
elif (card1[0] == card2[0] and card1[0] == card3[0]) or (card1[1] == card2[1] and card1[1] == card3[1]):
    print("Bonanza")
else:
    print("No Bonanza")